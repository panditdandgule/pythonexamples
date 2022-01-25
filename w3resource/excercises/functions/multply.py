def multiply(y):
    total = 1
    for x in y:
        total *= x
    return total


l = [8, 2, 3, -1, 7]
print("Multiplication of Numbers: ", multiply(l))
