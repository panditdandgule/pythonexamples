def fib():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 100:
        break
    print(f)
