def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end='')
    display(s,ind+1)

s = input()
print(display(s,0))