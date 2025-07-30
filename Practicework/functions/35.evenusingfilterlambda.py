n=list(map(int,input("Enter the numbers: ").split()))
l=list(filter(lambda n:n%2==0,n))
print(l)
#l=list(map(lambda n:n*n,n))