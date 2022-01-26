def count_string(items):
    count = 0
    for x in items:
        if len(x) > 2:
            if x[0] == x[-1]:
                count += 1
    return count


print("The Count Number of Strings: ", count_string(['abc', 'xyz', 'aba', '1221']))
