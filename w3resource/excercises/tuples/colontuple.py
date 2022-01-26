from copy import deepcopy

# create a tuple
tuplex = ("Hello", 5, [], True)
print(tuplex)

# Make copy of tuple using deepcopy() function
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)
