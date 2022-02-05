class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total+=x
        print("The total sum :",total)


t=Test()
t.sum(10,20,30,40)
t.sum(10,20)
t.sum()

