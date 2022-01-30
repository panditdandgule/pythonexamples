def outer():
    print("outer function started")
    def inner():
        print("inner function started")
    print("outer function returning inner function")
    return inner

f1=outer()
f1()
f1()