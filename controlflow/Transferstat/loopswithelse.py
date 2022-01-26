cart=[10,20,30,500,40,50]
for item in cart:
    if item>=500:
        print("We can not process this order")
        break
    print(item)

else:
    print("Congrates all items processed successfully..")