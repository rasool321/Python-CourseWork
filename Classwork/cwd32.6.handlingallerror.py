try:
    a=10
    a+=10
    l=[1,2,3,4]
    k=l[2]
    d={1:2,2:3,3:4}
    print(d[1])
    b=int(input('Enter a number:'))
    print(b)
    c=1+'12'

except Exception as e:
    print(f'Error occured:{e}')

'''
except (NameError,IndexError,ValueError,TypeError,KeyError) as e:
    print(f'Error occured: {e}')
'''