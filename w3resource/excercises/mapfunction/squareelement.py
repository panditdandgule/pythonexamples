list1=[2,3,4,5,6]

result=map(lambda x:x*x,list1)

print(list(result))

result1={x:x*x for x in list1}
print(result1)