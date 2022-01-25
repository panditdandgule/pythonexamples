def readfiles_linebyline(file):
    with open(file) as f:
        content_list=f.readlines()
        print(content_list,end="")


readfiles_linebyline('file.txt')
