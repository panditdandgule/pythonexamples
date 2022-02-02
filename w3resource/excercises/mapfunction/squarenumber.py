numbers = [2, 3, 4, 5, 6]


def squarenumber(x):
    return x * x


squarenumber_map = map(squarenumber, numbers)

print(list(squarenumber_map))
