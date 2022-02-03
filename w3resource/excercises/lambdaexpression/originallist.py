l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List: ", l)
print("\nEven List:")
evenlist = list(filter(lambda x: x % 2 == 0, l))
print(evenlist)
print("\nOdd List: ")
oddlist = list(filter(lambda x: x % 2 != 0, l))
print(oddlist)
