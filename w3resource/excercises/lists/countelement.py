def count_range_in_list(li, min, max):
    ctr = 0
    for x in li:

        # if min <=x <=max #it will work as and condition
        if min <= x:
            if x <= max:
                ctr += 1
    return ctr


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]

print(count_range_in_list(list1, 40, 100))
