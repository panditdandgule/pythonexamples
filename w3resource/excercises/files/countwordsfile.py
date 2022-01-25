from collections import Counter


def count_words(fname):
    with open(fname) as f:
        data = f.read().split()
        print(Counter(data))


count_words('file.txt')
