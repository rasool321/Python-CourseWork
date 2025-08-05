def countofdigit(n):
    if n==0:
        return 1
    elif n==1:
      return 1
    return 1+countofdigit(n//10)
n=int(input("Enter the number:"))
print(countofdigit(n))