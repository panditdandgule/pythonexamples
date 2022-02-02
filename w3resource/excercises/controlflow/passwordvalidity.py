import re

pwd = input("Enter valid password: ")
x = True
while x:
    if (len(pwd) > 6 or len(pwd) <= 16):
        break
    elif not re.search('[a-z]', pwd):
        break
    elif not re.search('[A-Z]', pwd):
        break
    elif not re.search('[0-9]', pwd):
        break
    elif not re.search('[$#@]', pwd):
        break
    elif not re.search('\s', pwd):
        break
    else:
        print("Password is valid")
        x = False

if x:
    print("No valid password")
