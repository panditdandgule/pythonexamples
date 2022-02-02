def myfunc(x):
    return len(x)


x = map(myfunc, ('apple', 'oranage', 'banana'))

for y in x:
    print(y)
