class Person:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setSalary(self,salary):
        self.salary=salary

    def getSalary(self):
        return self.salary

n=int(input("Enter number of persons: "))
for i in range(n):
    p=Person()
    name=input("Enter person name: ")
    p.setName(name)
    salary=float(input("Enter salary"))
    p.setSalary(salary)

    print("Hi,",p.getName())
    print("Your Salary :",p.getSalary())
    print()

