from collections import Counter

lettr = 'w3resource'
print(Counter(lettr))

d = {}
for x in lettr:
    d[x] = d.get(x, 0) + 1

print("letter: ", d)

str = 'w3resource'
my_dict = {}
for letter in str:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print("My Dict: ", my_dict)
