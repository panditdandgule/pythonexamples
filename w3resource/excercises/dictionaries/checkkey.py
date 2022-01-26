dic1 = {1: 20, 2: 20, 3: 30, 4: 50, 5: 60}

if 2 in dic1:
    print(True)

if 3 in dic1:
    print(True)

if 6 in dic1:
    print(False)

if 6 not in dic1:
    print(True)


def is_key_present(x):
    if x in dic1:
        print("Key is present in dictionary:", x)
    else:
        print("Key is not present in dictionary:", x)


is_key_present(15)
is_key_present(5)