def gcd(n,m):
    while m>0:
        r=n%m
        n=m
        m=r
    return n

n,m=map(int,input("Enter two numbers:").split())
print('GCD is:',gcd(n,m)) 