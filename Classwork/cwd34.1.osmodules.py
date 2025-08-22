import os
import shutil

print(os.getcwd())
'''
#crearting file
if not os.path.exists('OS'):
    os.mkdir('OS')
'''

#creating the multiple folders 
if not os.path.exists('OS'):
    os.makedirs('OS/DSDA')

'''
#removing the file(Only empty files or folders only..)
if os.path.exists('OS'):
    os.rmdir('OS')
'''
#removing files with non empty can be remoe using shutil
#shutil.rmtree('OS')
'''
#listing out the exitings files
files=os.listdir('.')
for i in files:
    print(i)
'''