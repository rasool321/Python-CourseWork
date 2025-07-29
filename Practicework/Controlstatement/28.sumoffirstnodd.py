n=int(input("Enter the number: "))
sum=0
for i in range(n):
    if i%2!=0:
        sum+=i
print(sum)