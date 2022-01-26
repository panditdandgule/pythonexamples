def unique_numbers(l):
    x=[]
    for i in l:
        if i not in x:
            x.append(i)
    return x



l=[1,2,3,3,3,3,4,5]
print("Unique Numbers:",unique_numbers(l))