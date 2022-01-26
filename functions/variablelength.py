'''
Sometimes we can pass variable number of arguments to our function,
such type of arguments are called variable length arguments.
we can declare variable length arguments with * symbol as follows
def f1(*n)

We can call this function by passing any number of arguments including
zero number. Internally all these values represented in the form of tuples.
'''

def sum(*n):
    total=0
    for n1 in n:
        total+=n1
    print("Sum: ",total)
sum(10,20,30,40)