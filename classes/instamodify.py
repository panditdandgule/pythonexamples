class Test:
    def __init__(self):
        self.a=10
        self.b=20


t=Test()
print("t",t.a,t.b)
t.a=888
t.b=999
t1=Test()
print("t",t.a,t.b)
print("t1",t1.a,t1.b)