def outer():
    print("Outer function started..")
    def inner():
        print("Inner function started..")
    print("outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
f1()
