def count(n,x):
    if len(n) == 0:
        return 0
    if n[0] == x:
        return 1 + count(n[1:], x)
    else:
        return count(n[1:], x)
n=list(map(int,input("Enter the list elements:").split()))
x=int(input("Enter the ele:"))
print(count(n,x))