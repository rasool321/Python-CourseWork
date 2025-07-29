n=int(input("Enter the number: "))
count=0
d=0
if n==0 :
    print(count)
if n<0:
    n=-n
while n>0:
    d = d%10
    count+=1
    n=n//10
print(f'count : {count}')