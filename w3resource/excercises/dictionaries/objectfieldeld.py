class Objectfield:
    def __init__(self):
        self.a = 20
        self.b = 30
        self.c = 40

    def do_something(self):
        pass


a = Objectfield()
print(a.__dict__)
