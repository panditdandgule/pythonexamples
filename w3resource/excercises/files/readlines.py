def file_read(fname):
    with open(fname,'r') as f:
        data=f.readlines()
        for line in data:

            print(line,end="")

file_read('file.txt')