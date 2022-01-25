def add_data(file):
    data=file.write('\nBalaji\n')

    print(data,end="")

file=open('file.txt','a')
add_data(file)