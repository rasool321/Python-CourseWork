try:
    file=open('xyz.txt','r')
except Exception as e:
    print(f'File is not there{e}')