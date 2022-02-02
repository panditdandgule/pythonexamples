list1=[10,20,30,40]
tup=(50,60,70,80)

print("Original List:",list1)
result=map(str,list1)
print("Modified List:",list(result))

print("Original Tuple:",tup)
result1=map(str,tup)
print("Modified List:",tuple(result1))