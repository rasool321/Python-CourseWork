n = int(input("Ente the size: "))
for i in range(n):
    for j in range(i+1):
        print('*',end =" ")
    print()

'''    col =0 (row = 0 + 1 for iteration)
row =0 *

    col =1 (row = 1 + 1 for iteration)
row =1 * *

    col =2 (row = 2 + 1 for iteration)
row =2 * * *

    col =1 (row = 3 + 1 for iteration)
row =3 * * * *

    col =1 (row = 4 + 1 for iteration)
row =4 * * * * *
'''

