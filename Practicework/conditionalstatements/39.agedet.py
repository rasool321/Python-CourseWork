age1, age2 = input("Enter two ages separated by comma: ").split(',')
age1 = int(age1)
age2 = int(age2)

if age1 == age2:
    print("Same age")
elif age1 > age2:
    print(f"{age1} is older")
else:
    print(f"{age1} is younger")
