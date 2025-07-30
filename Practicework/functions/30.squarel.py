def list_square(l):
    s=[]
    for i in l:
        s.append(i*i)
    return s
l=list(map(int,input("Enter list elements:").split()))
print(list_square(l))