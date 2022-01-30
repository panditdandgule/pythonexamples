'''
We can declare function inside another function,
such type of functions are called Nested function.
'''


def outer():
    print("outer function is started")

    def inner():
        print("Inner function is started")

    print("outer function calling inner function")
    inner()


outer()

########################################################################
# In the above example inner() function is local to outer() function   #
# and hence it is not possible to call directly from outside of outer()#
# function.                                                            #
########################################################################
