from itertools import combinations


def sub_lists(mylist):
    subs = []
    for i in range(0, len(mylist) + 1):
        new = [list(x) for x in combinations(mylist, i)]
        if len(new) > 0:
            subs.extend(new)
    return subs


l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print("Original list:")
print(l1)
print("S")
print(sub_lists(l1))
print("Sublist of the said list:")
print(sub_lists(l1))
print("\nOriginal list:")
print(l2)
print("Sublist of the said list:")
print(sub_lists(l2))
