# 1st way
def reverse_string(x):
    s = ''
    for y in x:
        s = y + s
    return s


print("Reverse String:", reverse_string("1234abcd"))


# 2nd way
def reverse_strings(x):
    return x[::-1]


print("Reversed string: ", reverse_strings("1234abcd"))


# 3rd way
def reverse(x):
    return ''.join(reversed(x))


print("Reversed: ", reverse("1234abcd"))
