def sumn(n):
    if n==0:
        return n
    return n+sumn(n-1)

n=int(input("Enter the number:"))
print(sumn(n))