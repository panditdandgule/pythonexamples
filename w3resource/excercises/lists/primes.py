def prime_numbers(num):
    prime_num = []
    prime_list = []
    for i in range(2, num + 1):
        if i not in prime_num:
            prime_list.append(i)
            for j in range(i * i, num + 1, i):
                prime_num.append(j)
    print("The following are prime numbers:    ", prime_list, "\nThe following are not prime numbers: ", prime_num)
    return prime_list, prime_num


n = int(input("Enter number length: "))
prime_numbers(n)
