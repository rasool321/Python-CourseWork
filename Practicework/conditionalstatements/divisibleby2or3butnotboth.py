n = int(input("Enter the number:"))
if n%2==0 and n%3==0:
    print(f'{n} is divisible by both 2 and 3.')
elif n%2==0:
    print(f'{n} is divisble by 2.')
elif n%3==0:
    print(f'{n} is divisible by 3.')
else:
    print(f"{n} is not divisible by neither 2 and nor 3.")