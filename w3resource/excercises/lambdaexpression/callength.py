weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days=filter(lambda a:a if len(a)==6 else '',weekdays)

for x in days:
    print(x)