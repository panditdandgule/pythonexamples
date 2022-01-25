s=input("Enter the string: ")
l=s.split()
li=[]
i=0

while i<len(l):
    li.append(l[i][::-1])
    i+=1

output=' '.join(li)
print(output)