class Test:
    a=10 #outside the class using var name
    def __init__(self):
        '''Inside the constructor using class name'''
        Test.b=20

    def m1(self):
        '''Inside the instance method using class Name'''
        Test.c=30

    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=50

    @staticmethod
    def m3():
        Test.e=60

t=Test()
print(t.__dict__)
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)