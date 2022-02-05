class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def display(self):
        del self.d

t=Test()
t.display()
print(t.__dict__)
del t.a
print(t.__dict__)
