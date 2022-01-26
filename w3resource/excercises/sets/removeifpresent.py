num_set=set([1,2,3,4,5,5,5,6,7,8])
print("Original Set: ",num_set)

num_set.remove(5)
print("After Removing: ",num_set)

num_set.discard(6)
print(num_set)

num_set.discard(8)
print(num_set)

num_set.discard(15)
print(num_set)

num_set.discard(4)
print(num_set)

num_set.discard(7)
print(num_set)