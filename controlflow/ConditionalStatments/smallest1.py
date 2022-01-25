x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))

if x<y and x<z:
    print("Smallest number: ",x)
elif y<z:
    print("It is smallest number: ",y)
else:
    print("It is smallest number: ",z)