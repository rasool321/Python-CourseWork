def s(n):
    sum=0
    for i in range(1,n+1):
       sum+=i
    return sum
n=int(input("Ente the num:"))
print(s(n))