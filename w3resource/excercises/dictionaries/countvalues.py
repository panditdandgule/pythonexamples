student = [{'id': 1, 'Success': True,  'Name': 'Larry'},
           {'id': 2, 'Success': False, 'Name': 'Rabi'},
           {'id': 3, 'Success': True,  'Name': 'Alex'}
           ]

print(sum(x['id'] for x in student))
print(sum(x['id'] for x in student))
print(sum(y['id'] for y in student))
