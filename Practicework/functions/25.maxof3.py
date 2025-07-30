def maxi(n,m,o):
    if n>m and n>o:
      return f"{n} is Greater than {m} and {o}"
    elif m>n and m>0:
      return f"{m} is Greater than {n} and {o}"
    else:
      return f"{o} is Greater than {m} and {n}"
n,m,o = input("Enter three numbers: ").split()
print(maxi(int(n),int(m),int(o)))