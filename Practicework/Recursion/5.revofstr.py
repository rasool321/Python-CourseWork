def revs(s,ind):
    '''if len(s)==0:
        return ''
    return s[-1]+revs(s[:-1])'''
    if ind<=0:
        return
    print(s[ind-1],end='')
    return revs(s,ind-1)

s=input("Enter the string:")
revs(s,len(s))