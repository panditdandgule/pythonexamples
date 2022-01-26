n=int(input("Enter numbers: " ))
print("The following 1 to",n,"prime numbers")
x=[]
for i in range(1,n+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        x.append(i)

print(x)
