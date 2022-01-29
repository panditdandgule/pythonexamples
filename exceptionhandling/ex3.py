try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("please provide valid number only",msg)
except:
    print("Please provide valid number only")