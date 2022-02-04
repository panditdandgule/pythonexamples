class Test:
    def __init__(self):
        self.eno=100
        self.ename='pandit'

    def m1(self):
        self.esal=100000

t=Test()
t.m1()
t.d=40
print(t.eno)
print(t.esal)
print(t.d)
del t.d

print(t.d)