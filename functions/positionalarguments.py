#These are the arguments passed to function in correct positional order

def sub(a,b):
    return a-b

#These are the positional arguments
print("Sub",sub(100,50))
print("Substraction",sub(100,20))

#######################################################################
# The number of arguments and position of arguments must be matched.  #
# If we change the order then result may be changed.                  #
# If we change the number of arguments then we will get error.        #
#######################################################################