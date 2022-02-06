class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def total(self):
        print(self.a)
        print(self.b)

    @classmethod
    def add(cls,c):
        print(c)

    @staticmethod
    def product(x,y):
        return x*y


t=Test(10,20)
print(t.__dict__)
t.total()
t.add(200)
print(Test.product(2,3))