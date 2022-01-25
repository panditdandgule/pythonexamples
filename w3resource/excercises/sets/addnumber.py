items = set()
# Add single element
items.add(10)
print("Adding single element: ", items)
items.add(20)
print("Adding single element: ", items)
# Add multiple elements
items.update(range(10), [10, 20, 30, 40, 50])
print("Adding multiple elementes: ", items)

num_set = set()
# add elements in set using loop
for x in range(1, 30, 2):
    num_set.add(x)

print("Adding multiple elements using add and loop: ", num_set)
