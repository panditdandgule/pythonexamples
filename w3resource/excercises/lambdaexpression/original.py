num=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Original Numbers: ",num)

d=list(filter(lambda x:x%19==0 or x%13==0,num))
print("Number divisible by ninteen and thirteen: ",d)