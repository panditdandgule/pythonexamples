import os
import sys

fname = input("Enter file name: ")
lines = 0
words = 0
ch = 0
if os.path.isfile(fname):
    print("File is exists", fname)
    with open(fname, 'r') as f:
        for line in f:
            lines = lines + 1
            ch = ch + len(line)
            word = line.split()
            words = words + len(word)
else:
    print("File does not exist", fname)
    sys.exit(0)

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of chars:", ch)
