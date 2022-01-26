def even_numbers(num):
    print("The Original list: ", num)
    odd = []
    for x in num:
        if x % 2 != 0:
            odd.append(x)

    return odd


print("Th Odd Numbers: ", even_numbers([1, 2, 3, 4, 6, 7, 8, 9, 10]))
