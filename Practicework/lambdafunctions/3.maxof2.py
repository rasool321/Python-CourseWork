n=int(input("Enter the number: "))
m=int(input("Enter the number: "))
l=lambda n,m: f'{n} Greater' if n>m else f"{m} Greater"
print(l(n,m))