dict_val=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

d=set()

for dic in dict_val:
    for val in dic.values():
        d.add(val)


print(d)