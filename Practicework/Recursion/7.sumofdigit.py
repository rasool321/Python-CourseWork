def sumofdigit(n):
    if n==0:
        return 0
    return n%10+sumofdigit(n//10)
n=int(input("Enter the number:"))
print(sumofdigit(n))