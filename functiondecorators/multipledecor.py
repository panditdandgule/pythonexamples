def my_decor(func):
    def my_wrap(*args,**kwargs):
        print("Decorator function1")
        return func(*args,**kwargs)
    return my_wrap

def my_another_decor(func):
    def my_wrap(*args,**kwargs):
        print("Decorator Function 2")
        return func(*args,**kwargs)

    return my_wrap

@my_decor
@my_another_decor
def my_function(str1,str2):
    print("Main Function")
    print(str1+"are"+str2)

my_function("Mangoes","Delicious")