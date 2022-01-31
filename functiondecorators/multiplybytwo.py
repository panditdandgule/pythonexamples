def multiply_by_two(method):
    def _multiply_by_two(a, b):
        return method(a, b)
    return _multiply_by_two

@multiply_by_two
def add(a,b):
    return a+b

print(add(10,5))

@multiply_by_two
def sub(a,b):
    return a-b

print(sub(10,5))

@multiply_by_two
def mul(a,b):
    return a*b

print(mul(10,5))