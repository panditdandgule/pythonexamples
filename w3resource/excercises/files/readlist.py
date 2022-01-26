def read_file(fname):
    content_array = []
    with open(fname, 'r') as f:
        for line in f:
            content_array.append(line.rstrip('\n'))

    print(content_array)


read_file('file.txt')
