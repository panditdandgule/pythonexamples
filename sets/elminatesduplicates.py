l=eval(input("Enter list: "))
l1=[]
l2=[]
for x in l:
    if x not in l1:
        l1.append(x)
    else:
        l2.append(x)

print("Unique Elements: ",l1)
print("Duplicates Elements: ",l2)