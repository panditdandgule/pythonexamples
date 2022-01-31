num_divisble = []
for num in range(1500, 2700):
    if num % 7 == 0 and num % 5 == 0:
        num_divisble.append(str(num))

print(','.join(num_divisble))
