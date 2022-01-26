import copy

num_set=set([1,2,3,4,5,5,6])
new_set=copy.copy(num_set)

print("Num Set:",num_set)
print("New Set: ",new_set)
print(id(num_set))
print(id(new_set))

new_set.add(7)
print("After modifying num set:",num_set)
print("After modifying new set: ",new_set)
print(id(num_set))
print(id(new_set))

num_set.add(8)
print("After modifying num set:",num_set)
print("After modifying new set: ",new_set)