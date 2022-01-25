setx = set(['Green', 'Blue'])
sety = set(['Blue', 'Yellow'])

print("Original Sets:")
print(setx)
print(sety)

result = setx - sety
print(result)

result1 = setx.difference(sety)
print(result1)

result2 = sety.difference(setx)
print(result2)
