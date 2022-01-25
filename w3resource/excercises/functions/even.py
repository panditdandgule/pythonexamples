def check_even(l):
    li = []
    for x in l:
        if x % 2 == 0:
            li.append(x)
    return li


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The Original Numbers are:", l)
print("The following are the even numbers:", check_even(l))
