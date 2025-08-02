def number(n):
    if n==0:
        return
    number(n-1)
    print(n)
n=int(input("Enter the number:"))
number(n)