list1 = list('abcdef')
list2 = list('defgh')

print("Missing Elements in List2: ", ','.join(set(list1).difference(list2)))
print("Additional Elements in List2: ", ','.join(set(list2).difference(list1)))
