nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list:",nums)

total_negative_nums=list(filter(lambda x:x<0,nums))
total_positive_nums=list(filter(lambda x:x>0,nums))

print("Total Negative Number:",sum(total_negative_nums))
print("Total Positive Number:",sum(total_positive_nums))