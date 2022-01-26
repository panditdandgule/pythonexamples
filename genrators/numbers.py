def numbers(num):
    n = 1
    # checking condition if n is less than or equal then generate sequence
    while n <= num:
        yield n
        n += 1


values = numbers(10)
for x in values:
    print(x)
