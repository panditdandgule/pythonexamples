def countdown(num):
    print("start countdown")
    while num > 0:
        yield num
        num -= 1


values = countdown(5)

for x in values:
    print(x)
