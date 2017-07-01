#! /usr/bin/python2.7

import sys, itertools, argparse, string, hashlib

if __name__ == '__main__' :
	words_hex = ["\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08"]
	words_ascii = ["0","1","2","3","4","5","6","7","8" ]

	parser = argparse.ArgumentParser(description = 'Android Pattern Cracker is program which cracks android pattern.')
	parser.add_argument('--mode', type = str, help = 'Select mode (mode = crack/generate)', choices = ['crack','generate'], required = True)
	parser.add_argument('--length', type  = int, choices= [4,5,6,7,8,9], help = 'Length of the pattern', default = 0)
	parser.add_argument('--file', type = str, help = 'Name of the pattern file.')
	parser.add_argument('--hex', type = str, help = 'HEX values of the pattern.')
	parser.add_argument('--write', type=str, help='In crack mode, outputs the pin to the file. In generate mode, ouput the sqlite database.', default = 'output')
	args = parser.parse_args()