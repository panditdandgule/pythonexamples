class Test:
    x=10
    def __init__(self):
        self.y=20

t=Test()
t2=Test()
print("t",t.x,t.y)
Test.x=999
print(t.x,t.y)
t.y=999

print(t.y,t2.y)