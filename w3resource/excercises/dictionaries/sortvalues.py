import collections

dict_maths={'Math':81, 'Physics':83, 'Chemistry':87}

ctr=collections.Counter(dict_maths)
print(ctr)
print(ctr.most_common())