def calculate_func(n):
    return lambda x: x * n


result = calculate_func(2)
print("The result is :", result(15))

result = calculate_func(3)
print("The result is :", result(15))

result=calculate_func(4)
print("The result is: ",result(15))

'''
r=lambda a:15*a

print(r(2))
print(r(3))
print(r(4))
print(r(5))

'''
