def common_member(list1, list2):
    for x in list1:
        for y in list2:
            if x==y:
                return True


list1 = [10, 20, 30, 40]
list2 = [40, 50, 60, 70]
print("The common element: ", common_member(list1, list2))
print("The common element: ", common_member([10,20,30,40], [50,60,70,80]))