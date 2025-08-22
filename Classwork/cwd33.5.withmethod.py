with open('abc.txt','r+') as file:
    file.write('File Operations')
    file.seek(0)
    print(file.read())
