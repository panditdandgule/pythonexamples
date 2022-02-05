class Test:
    a=777
    def __init__(self):

        Test.a=888

    def display(self):

        Test.a=1000

    @classmethod
    def m1(cls):
        cls.a=111
        Test.a=222

    @staticmethod
    def m2():
        Test.a=333


t=Test()
print(Test.a)
t.display()
print(Test.a)
t.m1()
print(Test.a)
t.m2()
print(Test.a)