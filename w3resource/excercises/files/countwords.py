def count_words(fname):
    with open(fname) as f:
        words=0
        data=f.read().split()
        for line in data:
            words+=1

    print("Total number of words:",words)

count_words('file.txt')