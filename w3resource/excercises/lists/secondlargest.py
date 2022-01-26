def largest(numbers):
    if (len(numbers) < 2):
        return
    if ((len(numbers) == 2) and (numbers[0] == numbers[1])):
        return
    dup_items = set()
    uniq_items = []
    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    uniq_items.sort(reverse=True)
    #print(uniq_items)
    return uniq_items[1]


print(largest([1, 2, -8, -2, 0, -2]))
print(largest([1, 1, 0, 0, 2, -2, -2]))
print(largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(largest([2, 2]))
print(largest([2]))
