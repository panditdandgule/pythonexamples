l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List: ", l)
print("\nSquare Of List: ")
sq = list(map(lambda x: x * x, l))
print(sq)
print("\nCube of List: ")
cu = list(map(lambda x: x ** x, l))
print(cu)
