s=input("Enter string:")
#for i in range(len(s)):
    #print("Character of index",i,"at",s[i],"and negative index",i-len(s),"at",s[i])

i=0
for x in s:
    print("The character present at positive index {} and negative index {} is {}".format(i,i-len(s),x))
    i+=1
