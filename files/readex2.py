f = open('abc.txt', 'r')
# read only first 10 characters
data = f.read(10)
print(data)
f.close()
