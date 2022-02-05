class Test:
    a=10
    def __init__(self):
        self.a=100

    def m1(self):
        self.a=888

t=Test()
t.m1()
print(Test.a)
print(t.a)
t.a=200
print(t.a)
print(Test.a)