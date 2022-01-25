#Sometimes we can provide defalult values for our positional arguments.

def wish(name="Guest",msg="Good morning"):
#def wish(name,msg="Good morning"):
    print("Hello",name,msg)

wish("Pandit",msg='Good Morning')
wish(name="bali",msg="good morning")

#If we are not passing any name then only default value will be considered