def sumofdigit(n):
    if n<=0:
        return n
    return (n%10)+sumofdigit(n//10)
n=int(input())
print(sumofdigit(n))