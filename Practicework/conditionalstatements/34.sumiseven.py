n , m = input("Enter the numbers:").split()
n = int(n)
m = int(m)
s= n+m
if s%2==0:
    print(f"sum of {n},{m} is {s}, is even :)")
else:
    print(f'sum of {n},{m} is {s}, is odd :(')