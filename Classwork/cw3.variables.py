#Variable Assignment
name = "Laptop"
age = 21
course = True
print(name,age,course) #Laptop 21 True

#Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c) # Output: 10 20 30

#assign the same value to multiple variables
x = y = z = 100
print(x, y, z) # Output: 100 100 100

#Reassignment
x = 5
x = 10
print(x) # Output: 10

#Swapping Variables
a, b = 5, 10
a, b = b, a
print(a, b) # Output: 10 5


#Deleting Variables
x = 100
del x
# print(x) # Raises: NameError: name 'x' is not defined