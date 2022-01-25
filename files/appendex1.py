f = open('abcd.txt', 'a')
li = ['sunny\n', 'bunny\n', 'chinny\n', 'vinny\n']
f.writelines(li)
print("List of lines written to the file successfully")
f.close()
