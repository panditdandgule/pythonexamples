def operations(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
x,y,z,l=operations(100,50)
print("The sum:",x)
print("The sub:",y)
print("The multiplication:",z)
print("The division:",l)