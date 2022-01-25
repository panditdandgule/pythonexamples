x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}
z = {8}
print("Original Set Elements: ")
print(x)
print(y)
print(z)

print("Confirm two given set no elements in common: ")
print("Compare x and y")
print(x.isdisjoint(y))
print("Compare y and x")
print(y.isdisjoint(x))
print("Compare x and z")
print(x.isdisjoint(z))
print("Compare y and z")
print(y.isdisjoint(z))
