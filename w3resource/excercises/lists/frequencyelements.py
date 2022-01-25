from collections import Counter

items = [10, 10, 10, 20, 30, 40, 40,10, 50, 50, 50, 50,50, 60, 60, 60]
print("Count Occurrences: ", Counter(items))
print("Most Common: ", Counter(items).most_common(1))
