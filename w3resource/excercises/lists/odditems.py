list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
result=[]
for x in range(len(list1)):
    if x % 2 != 0:
        print(list1[x],sep=',')


# second way
print()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[::2])
