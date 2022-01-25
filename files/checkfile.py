import os
import sys

fname = input("Enter file name:")

if os.path.isfile(fname):
    print("File exists", fname)
    f = open(fname, 'r')
else:
    print("File does not exists", fname)
    sys.exit(0)
print("The content of file is:")
data = f.read()
print(data)
f.close()
