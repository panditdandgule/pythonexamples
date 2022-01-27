dict_items = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

print("Original Dictionary")
print(dict_items)

new_dict = {}
for key, value in dict_items.items():
    if value >= 170:
        new_dict[key] = value

new_dict = {key: value for key, value in dict_items.items() if value >= 170}
print("Marks greater than 170:")
print(new_dict)
