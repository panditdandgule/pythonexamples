list_item1=['S001', 'S002', 'S003', 'S004']
list_item2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list_item3=[85, 98, 89, 92]

new_dict=[{x:{y:z}} for x,y,z in zip(list_item1,list_item2,list_item3)]

print(new_dict)