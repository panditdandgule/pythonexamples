def remove_duplicates(items):
    li = set()
    dups=[]

    for x in items:
        if x not in li:
            dups.append(x)
            li.add(x)


    return li,dups


num = [10, 20, 30, 10, 10, 40, 30]
print("The actual values:", num)
print("The unique values:", remove_duplicates(num))
