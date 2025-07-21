n = int(input("Ente the size: "))
for i in range(n):
    for j in range(n-i):
        print('*',end =" ")
    print()

'''    col =0 (row = 5 - 1 for iteration)
row =0 * * * * *

    col =1 (row = 5 - 1 for iteration)
row =1 * * * *

    col =2 (row = 5 - 1 for iteration)
row =2 * * *

    col =1 (row = 5 - 1 for iteration)
row =3 * * 

    col =1 (row = 5 - 1 for iteration)
row =4 * 
'''