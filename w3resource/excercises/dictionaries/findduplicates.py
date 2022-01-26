dict_num={1:{1:20,2:40},
          2:{1:20,2:50},
          3:{1:50,2:50}}

d={}
print("original Dictionary: ",dict_num)
for key,value in dict_num.items():
    if value not in d.values():
        d[key]=value
print("Unique dictionary: ",d)