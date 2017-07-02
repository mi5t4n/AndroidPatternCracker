# AndroidPatternCracker
It is a tool which cracks the android pattern.

    Usage: android_pattern_cracker.py [-h] --mode {crack,generate}
                                  [--length {4,5,6,7,8,9}] [--file FILE]
                                  [--hash HASH] [--write WRITE] [--verbose]

    Android Pattern Cracker is program which cracks android pattern.

    optional arguments:
      -h, --help            show this help message and exit
      --mode {crack,generate}
                            Select mode (mode = crack/generate)
      --length {4,5,6,7,8,9}
                            Length of the pattern
      --file FILE           Name of the pattern file.
      --hash HASH           SHA1 hash of the pattern.
      --write WRITE         In crack mode, outputs the pin to the file. In
                        generate mode, ouput the sqlite database.

# How does the android pattern works?
The android pattern is a sequence of length 3 (4 since Android 2.3.3) to 8 digits. The 3x3 matrix is given below

    -------------
    | 0 | 1 | 2 |
    -------------
    | 3 | 4 | 5 |
    -------------
    | 6 | 7 | 8 |
    -------------
The pattern is not stored directly as the sequence of digits but instead as the SHA1 hash of the pattern.
For example: if the pattern is 0 -> 4 -> 8 -> 5 -> 2. The SHA1 hash will be SHA1("\x00\x04\x08\x05\02") = 70d61edf47d85aaf53e089eafc74de0094754cc6

# Where can I find the hash?
The SHA1 hash of the pattern is stored in /data/system/gesture.key Y You can fetch the file using adb tool found in the Android SDK. Follow the following steps to fetch the gesture.key file.
    1. Enable developer mode and debugging
    2. Connect your phone to your computer.
    3. Use adb tool found in the platform-tools in Android SDK.
    Note: You must have root access to your phone.

    pc@user:~/android-sdk-linux/platform-tools$ ./adb pull /data/system/gesture.key .
    /data/system/gesture.key: 1 file pulled. 0.0 MB/s (20 bytes in 0.083s)
    
    pc@user:~/android-sdk-linux/platform-tools$ hd gesture.key
    00000000  23 a6 e7 c8 35 cd 75 c3  f1 7e cc 4d 1c d7 d8 40  |#...5.u..~.M...@|
    00000010  b7 40 95 25                                       |.@.%|
    00000014

# How to use the tool?
    pc@user:~/AndroidPatternCracker$ ./android_pattern_cracker.py --mode crack --file Pattern_Files/gesture_0.key
    [+] Opening pattern file (Pattern_Files/gesture_0.key) to read.
    [+] Pattern = 70d61edf47d85aaf53e089eafc74de0094754cc6
    [+] Closed pattern file (Pattern_Files/gesture_0.key)
    [+] Searching patterns of size = 3
    [+] Finished searching patterns of size = 3
    [+] Searching patterns of size = 4
    [+] Finished searching patterns of size = 4
    [+] Searching patterns of size = 5
    [!] Sucessfully cracked !!! The pattern is 04852
    [!] Pattern and Hex of the pattern are written to file successfully.
