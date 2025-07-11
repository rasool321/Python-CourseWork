n = int(input("Enter the number: "))
if n>30:
    print(f"{n} hot :(")
elif n>15 and n<30:
    print(f"{n} moderate :| ")
elif n<15:
    print(f'{n} is cold.... ooo')
else:
    print("no whether .. :)")