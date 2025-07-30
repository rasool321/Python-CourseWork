l=list(map(int,input("Enter the elements:").split()))
p=list(filter(lambda x: x % 3 == 0, l))
print(p)