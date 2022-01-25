#Function that calls itself is known as recursive function.
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

    

n=int(input("Enter valid number: "))
print("Factorial of ",n,"is",factorial(n))