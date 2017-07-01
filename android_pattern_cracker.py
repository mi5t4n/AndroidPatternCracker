#! /usr/bin/python2.7

import sys, itertools, argparse, string, hashlib

def write():
	print("Write")

def mode_crack_generate(words_hex, words_ascii, args):

	if (args.mode == 'crack' and args.file != None and args.hash == None):
		print("[+] Opening pattern file (" + args.file + ") to read.")
		fp_pattern = open(args.file, "rb");
		pattern_hex = fp_pattern.read();
		pattern_hex_str = pattern_hex.encode('hex')
		print ("[+] Pattern = " + pattern_hex_str)
		fp_pattern.close()
		print("[+] Closed pattern file (" + args.file + ")")
	elif (args.mode == 'crack' and args.file == None and args.hash != None):
		pattern_hex_str = args.hash
		print ("[+] Pattern = " + args.hash)
	elif (args.mode == 'crack'):
		print("[!] Error : Use either --file or --hash parameter. Do not use both at the same time.")
		return

	if (args.write != None):	
		fp = open(args.write, "w")
	
	if (args.length == 0):
		start, end = 4, 10
	else:
		start, end = args.length, args.length +1
	
	for size in range(start, end):
		isCracked = False
		if (args.mode == 'generate'):
			print("[+] Generating patterns of size = " + str(size))
		else:
			print('[+] Searching patterns of size = ' + str(size))
		permut_hex = itertools.permutations(words_hex, size)
		permut_ascii = itertools.permutations(words_ascii, size)

		while (True):
			try:
				item_hex = permut_hex.next()
				item_hex_str = string.join(item_hex,"")
				item_ascii = permut_ascii.next()
				item_ascii_str = string.join(item_ascii,"")

				item_hex_hash = hashlib.sha1(item_hex_str).hexdigest()
				out_text = item_ascii_str + " : "+ item_hex_hash
				if (args.mode == 'crack' and pattern_hex_str == item_hex_hash):
					isCracked = True
					print("[!] ###### Sucessfully cracked !!! The pattern is " + item_ascii_str + " #######")
					if (args.write != None):
						fp.write(item_ascii_str + "," + pattern_hex_str)
						print("[!] Pattern and Hex of the pattern are written to file successfully.")
					break
					
				if (args.verbose):
						print (out_text)
			except StopIteration:
				if (args.mode == 'generate'):
					print ("[+] Patterns and hashes of size = " + str(size) + " are generated.")
				else:
					print("[+] Finished searching patterns of size = " + str(size))
				break
		if (isCracked) :
			break	
	if (args.write != None):
		fp.close()

if __name__ == '__main__' :
	words_hex = ["\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08"]
	words_ascii = ["0","1","2","3","4","5","6","7","8" ]

	parser = argparse.ArgumentParser(description = 'Android Pattern Cracker is program which cracks android pattern.')
	parser.add_argument('--mode', type = str, help = 'Select mode (mode = crack/generate)', choices = ['crack','generate'], required = True)
	parser.add_argument('--length', type  = int, choices= [4,5,6,7,8,9], help = 'Length of the pattern', default = 0)
	parser.add_argument('--file', type = str, help = 'Name of the pattern file.')
	parser.add_argument('--hash', type = str, help = 'SHA1 hash of the pattern.')
	parser.add_argument('--write', type = str, default = 'output', help='In crack mode, outputs the pin to the file. In generate mode, ouput the sqlite database.')
	parser.add_argument('--verbose', action ='store_true')
	args = parser.parse_args()

	mode_crack_generate(words_hex, words_ascii, args)