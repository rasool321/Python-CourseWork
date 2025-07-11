n = int(input("Enter the number:"))
if n>=50 and n<100:
    if n%5==0:
        print(f"{n} is divisible by 5.")
    else:
        print(f'{n} is not divisible by 5..')
else:
    print(f"{n} is out of range.")