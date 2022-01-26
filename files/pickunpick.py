import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print(self.eno,self.ename,self.esal,self.eaddr)
with open("emp.dat",'wb') as f:
    e=Employee(100,"durga",1000,'Hyd')
    pickle.dump(e,f)
    print("Pickling of Employee object completed")

with open('emp.dat','rb') as f:
    obj=pickle.load(f)
    print("Printing Employee information after unpickling")
    obj.display()