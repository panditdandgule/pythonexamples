n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
n3=int(input("Enter third number: "))
if n1>n2 and n1>n3:
    print("It is biggest number: ",n1)
elif n2>n1 and n2>n3:
    print("It is biggest number: ",n2)
else:
    print("It is biggest number: ",n3)