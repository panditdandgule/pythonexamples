sum=lambda a,b:a+b
print("The sum of two numbers is ",sum(10,20))

big=lambda a,b:a if a>b else b
print("big number:",big(30,20))

small=lambda a,b:a if a<b else b
print("smallest: ",small(10,20))

even=lambda a:a%2==0
print("Even: ",even(4))