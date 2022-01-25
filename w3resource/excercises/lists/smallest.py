def smallest_numbers(items):
    small = min(items)

    for x in items:
        if small == x:
            small = x
    return small


print("The smallest number is:", smallest_numbers([90,30,40,10]))
