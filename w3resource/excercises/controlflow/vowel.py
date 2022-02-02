vowel = ('a', 'e', 'i', 'o', 'u')

while True:
    check = input("Check entered vowel:")
    if check in vowel:
        print("Its not consonant")
        continue
    else:
        print(check, "is consonant")
        break
