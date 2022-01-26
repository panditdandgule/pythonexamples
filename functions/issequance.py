def is_sequance(x):
    if x%2==0:
        return True
    else:
        return False

l=[0,5,10,15,20,25,30]
l1=filter(is_sequance,l)
print(list(l1))

even=filter(lambda l:l%2==0,l)
print(list(even))

odd=list(filter(lambda l:l%2!=0,l))
print(odd)

double=list(map(lambda l:2*l,l))
print("Double: ",double)

a=[1,2,3,4,5]
square=list(map(lambda a:a*a,a))
print(square)

from functools import *
b=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,b)
print("Reduce result",result)

total=reduce(lambda x,y:x+y,range(1,101))
print("Total: ",total)