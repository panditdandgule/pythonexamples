def largest_number(items):
    large = max(items)
    for x in items:
        if large == x:
            return x
        else:
            pass


print("The Largest Number from list: ", largest_number([10, 50, 60, 90]))
