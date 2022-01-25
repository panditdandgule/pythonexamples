d={1:20,2:20}

mul=1

for k,v in d.items():
    mul*=d.get(k,v)

print(mul)