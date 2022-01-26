def maximum_number(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter third number: "))
print("Max of number:", maximum_number(a, b, c))
