s=input("enter string")
l=s.split()
li=[]
i=len(l)-1

while i>=0:
    li.append(l[i])
    i=i-1

output=' '.join(li)
print(output)