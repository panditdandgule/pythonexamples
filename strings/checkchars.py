s=input("Enter any character: ")
if s.isalnum():
    print("Alpha numeric character")
elif s.isalpha():
    print("Alpha character")
elif s.isdigit():
    print("Digit character")
elif s.islower():
    print("Lower chars")
elif s.isupper():
    print("Upper charcs")
else:
    print("Empty character")