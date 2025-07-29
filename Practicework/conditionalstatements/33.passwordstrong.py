n = input("Enter your password:")
if len(n) >=8:
    print(f'{n} is a strong password..')
elif len(n)>=1 and len(n)<=7:
    print(f'{n} is weak password..')
else:
    print("give 7 more characters.")