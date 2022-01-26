"""
Enter number: 5
0
1
1
2
3
5
"""
n = int(input("Enter number: "))
a = 0
b = 1
i = 0

while i <= n:
    #printing values one by one
    print(a)
    a, b = b, a + b
    i += 1
