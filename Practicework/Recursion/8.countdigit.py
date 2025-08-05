def countofdigit(n):
    if n==0:
        return 0
    return 1+countofdigit(n//10)
n=int(input("Enter the number:"))
if n==0:
    print(1)
else:
    print(countofdigit(n))