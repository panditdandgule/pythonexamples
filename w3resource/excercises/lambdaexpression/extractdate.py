import datetime

now = datetime.datetime.now()
print(now)
year = lambda x: x.year
print(year(now))
ms = lambda x: x.month
print(ms(now))
ds = lambda x: x.day
print(ds(now))
second = lambda x: x.time()
print(second(now))
'''
x='2020-01-15 09:03:32.744178'

res=lambda x:x.split('-')

for y in res(x):
    print(y)
'''
