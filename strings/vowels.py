vowels=['a','e','i','o','u']
words=input("Enter the words to search vowels: ")
found=[]
for letter in words:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("The number of diffrent vowels present in",words,"is",len(found))