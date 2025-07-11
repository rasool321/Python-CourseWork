n,m = input("Enter the words:").split()
if len(n)>len(m):
    print(f"{n} is greater than {m}.")
elif len(n)<len(m):
    print(f"{m} is greater than {n}.")
else: 
    print(f"{n},{m} lenghts are same..")