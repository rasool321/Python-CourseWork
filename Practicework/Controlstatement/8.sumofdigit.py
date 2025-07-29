n=int(input("Enter the number:"))
sum=0
while n:
    re=n%10
    n=n//10
    sum+=re
print(sum)