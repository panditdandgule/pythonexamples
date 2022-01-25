d={1:10,2:20,3:30,4:40}

if 3 in d:
    print("Original dict",d)
    del d[3]
    print("after removing: ",d)

if 2 in d:
    print("Before: ",d)
    del d[2]
    print("After removing: ",d)