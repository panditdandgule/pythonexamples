def unique_values(l):
    print("Original List: ", l)
    result = set(l)
    return list(result)


items = eval(input("Enter list"))
print("List  Of Unique values: ", unique_values(items))
