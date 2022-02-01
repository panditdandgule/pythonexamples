word=input("Enter User Input: ")
print("original string:",word)
x=''
for i in word:
    x=i+x

print("Reversed string:",x)