try:
    file=open('demo.txt','r')

except Exception as e:
    print(f'File is not there{e}')

else:
    content = file.read() # Reads the entire content
    file.seek(0)
    lines = file.readlines() # Reads all lines into a list
    file.seek(0)
    line = file.readline() # Reads a single line
    print(f'\nFile Content using read():\n{content}')
    print(f'\nFile Content using readlines():\n{lines}')
    print(f'\nFile Content using readline():\n{line}')

finally:
    file.close()