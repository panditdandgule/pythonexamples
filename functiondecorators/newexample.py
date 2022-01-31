def my_decorator(func):
    def wrapper():
        print("Before doing something")
        func()
        print("After Decoration")

    return wrapper


def hello():
    print("welcome")


@my_decorator
def hello():
    print("Welcome..!")


# hello=my_decorator(hello)

hello()
