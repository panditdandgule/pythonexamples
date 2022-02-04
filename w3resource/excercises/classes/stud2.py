class Student:
    college='Modern College, Pune'
    def __init__(self,name,marks):
        self.studName=name
        self.studMarks=marks

    def display_stud_info(self):
        print("Student Name: ",self.studName)
        print("Student Marks: ",self.studMarks)

    def grade(self):
        if self.studMarks>=60:
            print("You are first class")
        elif self.studMarks>=50:
            print("You are second class")
        elif self.studMarks<=40:
            print("You are pass class")
        else:
            print("You are failed class")

print("Welcome to ",Student.college)
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter name of student: ")
    marks=float(input("Enter student marks: "))
    s=Student(name,marks)
    s.display_stud_info()
    s.grade()
    print()