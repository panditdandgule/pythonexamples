word=input("Enter Word: ")
vowel=list('aeiou')
d={}
for x in word:
    if x in vowel:
        d[x]=d.get(x,0)+1

for k,v in d.items():
    print(k,"occured",v,"times")