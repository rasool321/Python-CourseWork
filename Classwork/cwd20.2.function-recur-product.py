def product(n):
    if n==1:
        return 1
    return n * product(n-1)

n=int(input())
print(product(n))