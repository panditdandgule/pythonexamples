from collections import Counter

d = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = Counter()

for x in d:
    result[x['item']] += x['amount']

print(result)

result1 = Counter()
for i in d:
    result1[i['item']] += i['amount']

print(result1)

result2 = Counter()
for x in d:
    result2[x['item']] += x['amount']

print(result2)

result3 = Counter()
for x in d:
    result3[x['item']] += x['amount']

print(result3)

result4 = Counter()
for y in d:
    result4[y['item']] += y['amount']
print(result4)
