d={0: 10, 1: 20}

print("Original Dictionary: ",d)
d[2]=30

print("After Adding Dictionary: ",d)

d[3]=40
d[4]=50
d[5]=60
print("Updated Dictionary: ",d)

for x in range(70,150,10):
    d[x]=x
print("Updated Dictionary using Loop: ",d)