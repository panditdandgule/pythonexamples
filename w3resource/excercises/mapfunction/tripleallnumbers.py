num = [2, 3, 4, 5, 6, 7]

print("Original Numbers: ", num)
result = map(lambda num: num * 3, num)

print("Triple Numbers: ", list(result))
