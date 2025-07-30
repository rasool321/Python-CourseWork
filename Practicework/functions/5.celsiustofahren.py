def ctof(n):
    f=(c*9/5)+32
    return f'Temperature in Fahrenheit: {f}'
c=int(input("Enter temperature in Celsius:"))
print(ctof(c))