l1 = [10, 20, 30, 40]
l2 = [40, 50, 60, 70]


def addition_substraction(l1, l2):
    return l1 + l2, l1 - l2


print("Orignal List: ")
print(l1)
print(l2)
result = map(addition_substraction, l1, l2)

print("\nResult:")
print(list(result))
