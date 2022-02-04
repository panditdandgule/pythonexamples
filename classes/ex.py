class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def __str__(self):
        return f'{self.name}\t{self.rollno}\t{self.marks}'

    def talk(self):
        print("Hello I am",self.name)
        print("My rollno is: ",self.rollno)
        print("My marks are:",self.marks)

s=Student('Bali',11,89)
s1=Student('pandit',12,89)
s.talk()
print("\n")
s1.talk()
