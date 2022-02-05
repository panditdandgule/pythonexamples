class P:
    def property(self):
        print("Gold+Land+Cash+Power")

    def marry(self):
        print("Pandit")

class C(P):
    def marry(self):
        super().marry()
        print("Bali")

c=C()
c.marry()