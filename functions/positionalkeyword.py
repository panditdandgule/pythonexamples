'''
We can use both positional and keyword arguments simultenously.
But first we have to take positional arguments and then keyword
arguments, otherwise we will get syntax error.
'''

def wish(name,msg):
    print("Hello",name,msg)
    
wish("pandit",'Good Morning')
wish(name='bali',msg='Good morning')
wish('ravi',msg='Good Morning')
