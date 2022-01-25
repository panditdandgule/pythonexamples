"""
We can write character data to the text files by using the following 2 methods.
write(str)
writelines(list of lines)
"""

f = open('abcd.txt', 'w')
f.write('Durga\n')
f.write('Software\n')
f.write('Solutions\n')
print("Data written to the file successfully")
f.close()
