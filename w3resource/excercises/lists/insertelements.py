color = ['RED', 'GREEN', 'YELLO']
new_list = []
for ele in color:
    for v in ('c', ele):
        new_list.append(v)
# new_list=[v for ele in color for v in ('c',ele)]
print(new_list)
