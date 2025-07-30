def rem(l,e):
    l.remove(e)
    return l
l=list(map(int,input("Enter list elements: ").split()))
e=int(input("Enter element to remove: "))
print(rem(l,e))
    