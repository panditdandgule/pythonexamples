class Fruits:
    def __init__(self,ban):
        self.banana=ban

    def __str__(self):
        return f'I am {self.banana}'

    def __repr__(self):
        return f"Fruit'{self.banana}'"

b=Fruits('Banana')
print(b)
print(repr(b))