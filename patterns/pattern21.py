"""
J J J J J J J J J J
I I I I I I I I I
H H H H H H H H
G G G G G G G
F F F F F F
E E E E E
D D D D
C C C
B B
A

"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+n+1-i),end=" ")
    print()