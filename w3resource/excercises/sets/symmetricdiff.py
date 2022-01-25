setx = set(['Green', 'Blue'])
sety = set(['Blue', 'Yellow'])

# Excluding common
result = setx.symmetric_difference(sety)
print(result)
