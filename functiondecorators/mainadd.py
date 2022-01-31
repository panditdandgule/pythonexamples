def maindecor(func):
    def add(*args, **kwargs):
        return func(*args, **kwargs)

    return add


@maindecor
def sum(a, b):
    print("Result", a + b)


sum(10, 20)
