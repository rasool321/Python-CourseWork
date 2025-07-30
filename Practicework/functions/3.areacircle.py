def area(r):
    c = 3.14 * r * r
    return round(c, 2)

r = int(input("Enter the radius: "))
print("Area of circle is:", area(r))
