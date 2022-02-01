numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = []
odd = []

for x in numbers:
    if x % 2 != 0:
        odd.append(x)
    else:
        even.append(x)

print("The Even Number Count: ", len(even))
print("The Odd Number Count: ", len(odd))
