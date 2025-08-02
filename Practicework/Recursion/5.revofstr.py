def revs(s):
    if len(s)==0:
        return ''
    return s[-1]+revs(s[:-1])

s=input("Enter the string:")
print(revs(s))