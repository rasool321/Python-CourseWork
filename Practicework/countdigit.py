'''
if n>0 and n<10:
    print("len is 1")
if n>9 and n<100:
    print("len is 2")
if n>99 and n<1000:
    print("len is 3")
if n>999 and n<10000:
    print("len is 4")
if n>9999 and n<100000:
    print("len is 5")
if n>99999 and n<1000000:
    print("len is 6")

'''
n = int(input("Enter the number:"))
m = str(n)
if n<0:
    n = -n
elif n==0:
    print('1')
else:
    print(len(m))
