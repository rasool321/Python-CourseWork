n=int(input("Enter the number: "))
sum=0
for i in range(1,n):
    if n%i==0:
       sum+=i
if(sum==n):
    print("perfect number..")
else:
    print("Not a perfect number..")