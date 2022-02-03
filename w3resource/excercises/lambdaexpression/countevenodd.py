orginal=[1, 2, 3, 5, 7, 8, 9, 10]

print("Original Array: ",orginal)

even=list(filter(lambda a:a%2==0,orginal))
print("Number of even numbers in the above array: ",len(even))

odd=list(filter(lambda a:a%2!=0,orginal))
print("Number of odd numbers in the above array",len(odd))