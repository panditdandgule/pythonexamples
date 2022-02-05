class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self,other):
        return self.marks>other.marks

    def __le__(self,other):
        return self.marks<=other.marks

    def __lt__(self,other):
        return self.marks<other.marks

s=Student('pandit',50)
s1=Student('Bali',60)
print("Marks is greater than:",s1>s)
print("Marks is less than or equal:",s<=s1)
print("Marks is less than :",s<s1)