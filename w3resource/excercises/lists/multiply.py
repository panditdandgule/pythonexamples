def multiply(items):
    total = 1
    for x in items:
        total *= x
    return total


print("Multiplication Of All Numbers: ", multiply([10, 2, 3]))
