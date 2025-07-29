n=int(input("Enter the number:"))
temp=n
rev=0
while n:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)