def dou(l):
    r=[]
    for i in l:
        r.append(i*i) 
    return r

l=list(map(int,input("Enter list elements separated by space:").split()))
print(dou(l))