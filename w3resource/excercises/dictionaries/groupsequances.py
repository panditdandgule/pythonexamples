list_items = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

new_dict = {}
for key, value in list_items:
    new_dict.setdefault(key, []).append(value)

print(new_dict)
