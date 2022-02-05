class Test:
    def __init__(self,a=None,b=None):
        self.a=a
        self.b=b
        print("Constructor overloaded with default arguments.")



t=Test(10,30)
print(t.__dict__)
t1=Test(10)
print(t.__dict__)
t2=Test(10,40)
print(t.__dict__)