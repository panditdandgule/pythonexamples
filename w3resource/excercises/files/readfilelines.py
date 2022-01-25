def read_fileshead(f,lines):
    from itertools import islice
    with open(f) as f:
        for x in islice(f,lines):
            print(x,end="")


read_fileshead('file.txt',2)