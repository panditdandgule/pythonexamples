def fib(n):
    a,b=0,1
    i=0
    while i<=n:
        print(a)
        a,b=b,a+b
        i+=2
fib(10)

