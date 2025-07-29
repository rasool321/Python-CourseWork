n=int(input("Enter the number: "))
rev=0
d=0
while n>0:
    d=n%10
    if d%2==0:
        rev=rev*10+d
    n=n//10
print(f"rev of even :{rev}")

