class Student:
    def __init__(self, name, rollno, marks):
        self.studName = name
        self.rollNo = rollno
        self.marks = marks

    def __str__(self):
        return "Student Name: {}\tRollNo: {}\tMarks: {}".format(self.studName, self.rollNo, self.marks)

    def setName(self):
        self.studName = 'Bali'

    def getName(self):
        return self.studName

    def display_stud_info(self):
        print("Student Name:", self.studName)
        print("Student RollNo:", self.rollNo)
        print("Student Marks:", self.marks)


s = Student("pandit", 1, 90)
print(s)
s.display_stud_info()
print(Student.__dict__)
