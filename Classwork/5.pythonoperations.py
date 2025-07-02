#python operations
#Arthematic operations
a = 10
b = 20
print("Addition(+): ",a+b) #Addition(+):  30
print("Subtraction(-): ",a-b) #Subtraction(-):  -10
print("Muliplication(*): ",a*b) #Muliplication(*):  200
print("Division(/): ",a/b) #Division(/):  0.5
print("Floor Division(//):",a//b) #Floor Division(//): 0
print("Modulo(%)",a%b) #Modulo(%) 10
print("Exponential(**): ",a**b) #Exponential(**):  100000000000000000000

#comparision operations
print("Equal to (==)",a==b) #Equal to (==) False
print("Not Equal to (!=)",a!=b) #Not Equal to (!=) True
print("Greater than (>): ",a>b) #Greater than (>):  False
print("Less than (<):",a<b) #Less than (<): True
print("Greater than or Equal to (>=)",a>=b) #Greater than or Equal to (>=) False
print("Less than or Equal to (<=)",a<=b) #Less than or Equal to (<=) True

#Assignment operations 
a=20
print("Assign (=):",a ) #Assign (=): 20
a+=2
print("Add & Assign (+=):",a ) #Add & Assign (+=): 22
a-=2
print("Subtract & Assign (-=):", a) #Subtract & Assign (-=): 20
a*=2
print("Multiply & Assign (*=):",a ) #Multiply & Assign (*=): 40
a/=2
print("Divide & Assign (/=):", a) #Divide & Assign (/=): 20.0
a//=2
print("Floor Divide & Assign (//=):", a) #Floor Divide & Assign (//=): 10.0
a%=2
print("Modulus & Assign (%=):", a) #Modulus & Assign (%=): 0.0
a**=2
print("Exponentiate & Assign (**=):", a) #Exponentiate & Assign (**=): 0.0

#logical operations
a=10
b=20
print("AND:",a%2==0 and b%3==0) #AND: False
print("OR:",a%2==0 or b%3==0) #OR: True
print("not:",not b%5==0) #not: False

#Membership Operators
a = 'rasool'
print('a' in a) # in True
print('a' not in a) #false

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True

#Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the same object)
print(a is c) # Output: False (Different objects with the same content)
print(a is not c) # Output: True

#Logical operators
a = 5 # Binary: 0101
b = 3 # Binary: 0011
print(a & b) # Output: 1 (Binary: 0001 → AND operation)
print(a | b) # Output: 7 (Binary: 0111 → OR operation)
print(a ^ b) # Output: 6 (Binary: 0110 → XOR operation)
print(~a) # Output: -6 (Binary: Inverts bits of 5)
print(a << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(a >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)