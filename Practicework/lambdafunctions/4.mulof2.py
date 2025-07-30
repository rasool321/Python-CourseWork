n=int(input("Enter the number: "))
m=int(input("Enter the number: "))
l=lambda n,m: f'Multiple of {n},{m}: {n*m}'
print(l(n,m))