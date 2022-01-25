def decor(func):
    def inner(name):
        if name == 'Sunny':
            print("Hello Sunny Bad Morning")
        else:
            func(name)

    return inner



def wish(name):
    print("Hello", name, "Good Morning")

decorfunction=decor((wish))
wish("Durga")
wish("Ravi")
wish("Sunny")

decorfunction("pandit")
decorfunction("Sunny")