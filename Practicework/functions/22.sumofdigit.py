def sumofdigit(n):
    sum=0
    d=0
    while n>0:
        d=n%10
        sum+=d
        n=n//10
    return sum
n=int(input("Enter the number: "))
print(sumofdigit(n))