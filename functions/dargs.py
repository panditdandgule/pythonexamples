def f1(n1,*s):
    print(n1)
    for x in s:
        print(x)

f1("Positional Args:",50)
f1("Default Args:",10,20,30)
f1("Default Args:",70,20)

'''
After variable length argument, if we are taking any other arguments then
we should provide values as keyword arguments.
'''