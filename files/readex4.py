# To read all lines into list

f = open('abc.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()
