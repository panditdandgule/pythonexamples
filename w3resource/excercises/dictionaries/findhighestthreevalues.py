from heapq import nlargest

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
threevalue = nlargest(3, my_dict, key=my_dict.get)
print(threevalue)

from heapq import nlargest

d={1:20,2:30,3:40,5:50,6:60}
my_d=nlargest(1,d,key=d.get)
print(my_d)

dx={'name':'pandit','age':32,'salary':50000}
dx_h=nlargest(1,d,key=d.get)
print(dx_h)

high={1:3000,2:4000,3:9999884,4:97548759842}
high_val=nlargest(1,high,key=high.get)
print("Highest Value:",high_val)

height={'a':3443,'b':3452,'c':34152,'d':545123}
height_dict=nlargest(1,height,height.get)
print(height_dict)