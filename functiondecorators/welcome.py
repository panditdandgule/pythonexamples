def welcome(func):
    def inner():
        print("Starting..")
        func()
        print("Ending..")
    return inner


@welcome
def hello():
    print("Welcome")

hello()