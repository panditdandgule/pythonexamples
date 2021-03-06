def smart_division(func):
    def inner(a, b):
        print("we are dividing ", a, "with", b)
        if b == 0:
            print("OOPS.. cannot divide")
            return
        else:
            return func(a, b)

    return inner


@smart_division
def division(a, b):
    return a / b


print(division(10, 5))
print(division(10, 0))
