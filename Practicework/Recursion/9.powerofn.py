def powern(n,m):
    if m==0:
       return 1
    elif m==1:
       return n
    return n*powern(n,m-1)
n,m=input("Enter the numbers: ").split(',')
print(powern(int(n),int(m)))