#We can pass argument values by keyword that is by parameter name.

def wish(name,msg):
    print("Hello",name,msg)

wish(name='pandit',msg='Good Morning')
wish(msg="Good Morning",name="bali")

###################################################################
# Here is order of arguments is not important but number of       #
# arguments must be matched                                       #
###################################################################