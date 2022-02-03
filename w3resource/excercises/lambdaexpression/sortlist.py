lot=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original List Of Tuple: ",lot)
lot.sort(key=lambda x:x[1])
print("Sorted List of Tuple: ",lot)

print("\n")
lt=[('a',20),('b',25),('c',10),('d',5)]
print("Original List Of Tuple: ",lt)
lt.sort(key=lambda y:y[1])
print("Sorted List Of Tuple: ",lt)