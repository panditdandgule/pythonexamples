s = input("Enter string:")

numcount = 0
charcount = 0

for x in s:
    if x.isalpha():
        charcount += 1
    elif x.isdigit():
        numcount += 1
    else:
        pass
print("Char Count: ", charcount)
print("Number Count :", numcount)
