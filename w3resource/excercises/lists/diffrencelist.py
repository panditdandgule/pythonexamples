def difference_list(l1, l2):
    diff_l1_l2 = list(set(l1) - set(l2))
    diff_l2_l1 = list(set(l2) - set(l1))
    l3 = diff_l1_l2 + diff_l2_l1
    return l3


l1 = [10, 20, 30, 40, 50]
l2 = [40, 50, 60, 70, 80]
print("The difference of two list:", difference_list(l1, l2))
