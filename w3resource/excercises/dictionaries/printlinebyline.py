names={'India':{'Maharashtra':'Pune',
                'Rajastan':'Jaypur'},
       'USA':{'Birmingam':'New'}}

for a in names:
    print(a)
    for b in names[a]:
        print(b,":",names[a][b])