def remove_specifiedlist(items):
    print("The original items: ", items)
    new_list = []

    for x in items:
        if x == items[0] or x == items[4] or x == items[5]:
            continue
        else:
            new_list.append(x)
    return new_list


print("The Number of items after removing: ",
      remove_specifiedlist(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
