import sys
class Customer:
    '''Customer class with bank operations'''
    bankname='HDFC'
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance After deposit",self.balance)

    def withrow(self,amt):
        if amt>self.balance:
            print("Insufficient Funds.. cannot perform this operation..")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance after withdraw",self.balance)

print("Welcome to",Customer.bankname)
name=input("Enter your name: ")
amount=float(input("Enter your amount:"))
c=Customer(name,amount)

while True:
    print("Choose option:")
    print("d-deposit\nw-withraw\ne-exit")
    option=input("Enter your option:")
    if option=='d' or option=='D':
        amt=float(input("Enter your amount: "))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("Enter your amount: "))
        c.withrow(amt)
    elif option=='e' or option=='E':
        print("Thanks for banking..")
        sys.exit()
    else:
        print("Invalid option.. Please try again..")


