def longest_word(fname):
    w = 0
    d = {}
    with open(fname) as f:
        words = f.read().split()
        print(words)

    for word in words:
        d[word] = len(word)

    print(d)


longest_word('file.txt')
