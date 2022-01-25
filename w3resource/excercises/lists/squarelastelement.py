square = {}

for num in range(1, 21):
    if num > 5:
        square[num] = num ** 2
print("The square of element except five:", square)
