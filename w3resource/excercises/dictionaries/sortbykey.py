import operator

d={5:50,3:30,4:40,2:20,1:10}
print("original dictionary: ",d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print("After Sorting: ",sorted_d)

for k,v in d.items():
    print(k,v)
for key in sorted(d):
    print(key,":",d[key])
