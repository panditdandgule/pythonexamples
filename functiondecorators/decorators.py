import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam=return_greeting("Adam")
print(hi_adam)