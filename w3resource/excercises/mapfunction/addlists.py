l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
print(l1)
print(l2)
print(l3)

result = map(lambda l1, l2, l3: l1 + l2 + l3, l1, l2, l3)
print("\nNew List after adding above three lists:")
print(list(result))
