class Test:
    a=10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c=30

    @classmethod
    def m2(cls):
        cls.d=40
        Test.e=50

    @staticmethod
    def m3():
        Test.f=60

t=Test()
print(t.a)
print(Test.a)
print(Test.__dict__)
print(Test.b)
print(t.m1())
print(type(Test.c))