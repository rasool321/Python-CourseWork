def cl(l):
    l.clear()
    return l

l=list(map(int,input("Enter list elements separated by space:").split()))
print(cl(l))