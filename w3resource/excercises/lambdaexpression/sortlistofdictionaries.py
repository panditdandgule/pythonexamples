lod = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
       {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Original List Of Dictionary: ", lod)
print("\n")
re = sorted(lod, key=lambda x: x['color'])
print("Sorted List of Dictionary: ")
print(re)
