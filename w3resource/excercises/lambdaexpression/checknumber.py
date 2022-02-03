result = lambda x: x.replace('.', '', 1).isdigit()

print(result('1'))
print(result('one'))
print(result('132.45'))
result1 = lambda y: True if y.isdigit() else False
print(result1('1343'))
print(result1('one two'))
