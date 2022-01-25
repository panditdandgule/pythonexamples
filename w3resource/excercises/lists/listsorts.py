def last(n):
    return n[-1]


def sorted_list(items):
    return sorted(items, key=last)


print("The Sorted List: ", sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
