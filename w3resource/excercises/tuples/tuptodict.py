#create a tuple
tuplex=((2,'w'),(3,'r'))

print(dict((y,x) for x,y in tuplex ))

tup=(('name','pandit'),('age',29),('city','pune'))

print(dict((x,y) for x,y in tup))