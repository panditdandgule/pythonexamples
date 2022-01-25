d={}
n=int(input("Enter number of students:"))
i=0
while i<=n:
    name=input("Enter Name:")
    marks=input("Enter Marks:")
    d[name]=marks
    i+=1

print("Name of student\t","\t %of marks")
for k,v in d.items():
    print("\t",k,"\t\t",v)

