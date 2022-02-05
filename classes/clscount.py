class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noOfObject(cls):
        print("The number of object created test class",cls.count)

t1=Test()
t2=Test()
Test.noOfObject()
t3=Test()
t4=Test()
Test.noOfObject()