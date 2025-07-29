a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid Triangle ")
else:
    print("Invalid Triangle")
