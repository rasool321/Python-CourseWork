def display(s,ind):
    if ind==len(s)-lens+1:
        return
    print(s[ind:ind+lens])
    display(s,ind+1)

s='abcde'
lens=3
display(s,0)