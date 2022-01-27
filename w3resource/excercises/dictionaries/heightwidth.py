dict_items = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68),
              'Pierre Cox': (5.8, 66)}

print("Original Dictionary:")
print(dict_items)

for key, value in dict_items.items():
    if value[0] >= 6 and value[1] >= 70:
        print(key, value)

dict_val = {key: value for key, value in dict_items.items() if value[0] >= 6 and value[1] >= 70}
print("\nHeight > 6ft and Weight> 70kg:")
print(dict_val)
