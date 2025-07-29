n=int(input("Enter the number:"))
product=1
while n>0:
    d = n%10
    product = product * d
    n = n//10
print(product)
