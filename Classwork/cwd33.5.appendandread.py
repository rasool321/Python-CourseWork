try:
    file=open('abc.txt','a+')

except Exception as e:
    print(f'File is not there{e}')

else:
    file.write('Monday is a holiday')
    file.write('Samanth is a independent women!!')
    file.write('sam jam!!')
    file.seek(0)
    print(file.read())
finally:
    file.close()
