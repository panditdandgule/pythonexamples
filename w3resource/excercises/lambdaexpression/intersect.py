x=[1, 2, 3, 5, 7, 8, 9, 10]
y=[1, 2, 4, 8, 9]

res=lambda x,y:set(x) & set(y)
print(res(x,y))

r=list(filter(lambda a:a in x,y))
print(r)