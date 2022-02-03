x=[-1, 2, -3, 5, 7, 8, 9, -10]
print("Original Array: ",x)
r=list(filter(lambda a:a>1,x))
y=list(filter(lambda a:a<1,x))
print("Rearranging Array: ",str(r+y))

print("\n")
#2nd way
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)
