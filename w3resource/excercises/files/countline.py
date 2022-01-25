def count_lines(fname):
    with open(fname) as f:
        lines=0
        for line in f:
            lines+=1

    print("Total number of lines:",lines)

count_lines('file.txt')