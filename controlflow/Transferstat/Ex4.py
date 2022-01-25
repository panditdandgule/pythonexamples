cart=[10,20,500,700,50,60]
for item in cart:
    if item>=500:
        print("We can't process this item",item)
        continue
    print(item)