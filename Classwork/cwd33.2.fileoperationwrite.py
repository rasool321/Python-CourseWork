try:
    file=open('abc.txt','w')

except Exception as e:
    print(f'File is not there{e}')

else:
    file.write('Monday is a holiday')
    file.write('Samanth is a independent women!!')
finally:
    file.close()
