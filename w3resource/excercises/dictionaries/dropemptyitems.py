dict_items = {'c1': 'Red', 'c2': 'Green', 'c3': None}

dict_new = {}
for key, value in dict_items.items():
    if value is not None:
        dict_new[key] = value

print("Original Dictionary: ", dict_items)
print("Dictionary Items Not None: ", dict_new)
