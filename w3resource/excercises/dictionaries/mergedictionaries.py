dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
dict_str = {'A': 64, 'B': 65, 'C': 66,'D':67}

print("Dictionary First: ", dict_num)
print("Dictionary Second: ", dict_str)

new_dict = {**dict_num, **dict_str}

print("Combining Dictionaries: ", new_dict)
