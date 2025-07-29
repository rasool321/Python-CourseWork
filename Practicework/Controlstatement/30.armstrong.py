n=int(input("Enter the number:"))
s=0
p=len(str(n))
for i in str(n):
    s+=int(i)**p
if s==n:
    print("Armstrong")
else:
    print("Not a armstrong")
