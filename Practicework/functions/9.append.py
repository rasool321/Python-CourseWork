def app(l,e):
    l.append(e)
    return l

l=list(map(int,input("Enter list elements separated by space:").split()))
e=int(input("Enter element to append:"))
print(app(l,e))