n = int(input("Enter the 1 num"))
m = int(input("Enter the 2 num"))
o = int(input("Enter the 3 num"))
if n>m and n>o:
    print(f"{n} is Greater than {m} and {o}")
elif m>n and m>0:
    print(f"{m} is Greater than {n} and {o}")
else:
    print(f"{o} is Greater than {m} and {n}")