a=0

while(a<=20):
    i=1
    count=0
    while(i<=0):
        if a%i==0:
            count+=1
            i=i+1
    if count==2:
        print(a)
    a+=1
    
