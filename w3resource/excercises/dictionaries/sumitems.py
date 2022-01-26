d = {1: 20, 2: 30, 3: 30, 4: 40}
total = 0
for k, v in d.items():
    total += d.get(k, v)

print("The Total: ", total)

print("The Sum: ", sum(d.values()))
