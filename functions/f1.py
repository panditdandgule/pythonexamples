a=10 #global

def f1():
    global a
    a=777
    print(a)

def f2():
    print(a)

f1()
f2()