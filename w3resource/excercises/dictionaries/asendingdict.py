import operator

d={1:2,0:4,2:5,3:7,5:9,4:9}
print("Original Dictionary:",d)
sorted_d=sorted(d.items(), key=operator.itemgetter(1))
print("Sorted Dictionary: ",sorted_d)