set_x = set([1, 2, 3, 4, 5])
set_y = set([4, 5, 6, 7, 8])

print("Original Set_x: ", set_x)
result_x = set_x.intersection(set_y)
print(result_x)
print("Original set_x", set_x)

result_y = set_y.intersection(set_x)
print(result_y)

setx = set(['Green', 'Blue'])
sety = set(['Blue', 'Yellow'])
print("Original Sets:")
print(setx)
print(sety)
result = setx & sety
print("Intersection Results: ", result)
result1 = setx.intersection(sety)
print("Intersection Results: ", result1)
