# For existing function we can give another name, which is nothing but function aliasing

def wish(name):
    print("Good Morning", name)


greeting = wish

print(id(wish))
print(id(greeting))

greeting('durga')
wish('durga')

#####################################################################################
# In the above example only one function is available but we can call that function #
# by using either wish name or greeting name.                                       #
#                                                                                   #
# If we delete one name still we can access that function by using alias name       #
#####################################################################################
