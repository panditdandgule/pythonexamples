def concate_list(n, items):
    new_list = ['{}{}'.format(x, y) for y in range(0, n + 1) for x in items]
    print(new_list)


list1 = ['p', 'q']
concate_list(5, list1)
