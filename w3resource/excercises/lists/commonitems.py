def common_items(list1, list2):
    # first_list1 = set(list1).intersection(list2)
    common_elements = set(list1) & set(list2)
    return list(common_elements)


list1 = [10, 20, 30, 40, 50]
list2 = [40, 50, 60, 70, 80]
print("The common items: ", common_items(list1, list2))
