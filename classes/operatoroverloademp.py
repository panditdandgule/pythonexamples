class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self,other):
        return self.salary*other.days


class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

e=Employee('pandit',20000)
t=Timesheet('pandit',25)
print("Salary of number of days: ",e*t)