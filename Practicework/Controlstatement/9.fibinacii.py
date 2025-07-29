n = int(input("Enter the number:"))

if n == 0:
    f = 0
elif n == 1:
    f = 1
else:
    n0 = 0  
    n1 = 1  
    f = 0   
    for i in range(2, n + 1):  
        f = n0 + n1
        n0 = n1
        n1 = f
print(f)