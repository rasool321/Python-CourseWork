a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)
'''
(or)
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = math.gcd(a, b)
print("GCD is:", gcd)

 
'''