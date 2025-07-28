'''
def display(s,ind):
    if ind==-1:
        return
    print(s[ind],end='')
    display(s,ind-1)

s = input()
print(display(s,len(s)-1))

'''
def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end='\t')
    display(s,ind+1)
    print(s[ind],end='\t')
s = input()
print(display(s,0))
