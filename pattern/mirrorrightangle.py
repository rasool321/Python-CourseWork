n = int(input("Ente the size: "))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end =" ")
    for j in range(i):
        print('*',end =" ")
    print()