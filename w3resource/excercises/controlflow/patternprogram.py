n = int(input("Enter Number: "))
for i in range(n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n + 1):
    for j in range(i, n + 1):
        print("*", end=" ")
    print()
