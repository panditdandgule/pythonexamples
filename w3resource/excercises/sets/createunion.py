setx=set(['Green','Yellow',"Blue"])
sety=set(['Blue','Dark','Yellow'])

print("Original Sets: ")
print(setx)
print(sety)

result=setx|sety
print(result)

result1=setx.union(sety)
print(result1)
result2=sety.union(setx)
print(result2)