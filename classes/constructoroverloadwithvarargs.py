class Test:
    def __init__(self,*args):
        print("Constructor overloaded with variable length arguments")


t=Test()
t1=Test(10,20,30)
t2=Test(10,20,30,40)
t3=Test(10,20,30,40,50)