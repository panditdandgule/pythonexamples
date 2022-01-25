dict_num = {1: 20, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80}
print("KEY VALUE COUNT")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key, '   ', value, '  ', count)
