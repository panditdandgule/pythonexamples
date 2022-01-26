numbers = []
for num in range(1, 31):
    if num <= 5 or num >= 25:
        numbers.append(num ** 2)
print("The square up to 1 to 5:",numbers[:5])
print("The square up to 25 to 30:",numbers[5:])
