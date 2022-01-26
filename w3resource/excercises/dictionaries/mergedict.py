dic1={1:10,2:20,3:30}
dic2={4:40,5:50,6:60}
dic3=dict()

for x in (dic1,dic2):
    dic3.update(x)

print(dic3)

d=dic1.copy()
d.update(dic2)

print(d)