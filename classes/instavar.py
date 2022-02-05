class InstaVar:
    def __init__(self):
        '''using constructor we can create instance variable'''
        self.a=10
        self.b=20
        self.c=30

    def display(self):
        '''using self variable we can create instance var'''
        self.d=40
        '''we can access instance var using self'''
        print("A:",self.a)
        print("B:",self.b)

i=InstaVar()
i.display()
print(i.__dict__)
i.e=50 #using object refrence will create instance variable
print("C:",i.c)
print(i.__dict__)