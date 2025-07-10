# conditional statements
#if and else case
items  = ['shoes','smartwatch','phone','airpods']
print("Welcome to Amazon store ..".center(50,"*")) #************Welcome to Amazon store ..************
searchinput = input("enter :") #enter :shoes
if searchinput in items:
    print(f"{searchinput} found.Buy now!!!") #shoes found.Buy now!!!
else:
    print(f"{searchinput} is out of stock now.we will notify you") #snack is out of stock now.we will notify you

