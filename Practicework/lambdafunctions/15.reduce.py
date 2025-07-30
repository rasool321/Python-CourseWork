from functools import reduce
l=list(map(int,input("Enter the elements:").split()))
p=reduce(lambda x,y: x*y , l)
print(p)