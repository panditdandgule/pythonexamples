word=input("Enter word: ")
d={}
vowel=list('aeiou')

for x in word:
    if x in vowel:
        d[x]=d.get(x,0)+1

for k,v in sorted(d.items()):
    print(k,"occured",v,"times")