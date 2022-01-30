def addition(func):
    def add(*args,**kwargs):
        func(*args,**kwargs)


    return add




@addition
def sum(a,b):
    print("Addition:",a+b)

@addition
def sub(a,b):
    print("Sub b-a: ",b-a)

sum(10,20)
sub(20,40)