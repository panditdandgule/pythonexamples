n=int(input("Enter number of students: "))
d={}

for x in range(n):
    name=input("Enter Name: ")
    marks=int(input("Enter student marks: "))
    d[name]=marks

while True:
    name=input("Enter Student Name to get Marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("Studnet name not found")
    else:
        print("The marks of ",name,"are",marks)
    option=input("Do you want to find another student[Yes|No]")
    if option=='No':
        break
print("Thanks for using this app")