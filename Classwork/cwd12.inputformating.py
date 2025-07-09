#String Input
name = input("Enter your full name: ")
print(name) #Enter your full name: rasool
            #rasool
#Integer Input
item = int(input("Enter the number of items: "))
print(item) #Enter the number of items: 12
            #12
#Float Input
discount = float(input("Enter the number of discount: "))
print(discount) #Enter the number of items: 12.0
                #12.0
#Input as List (Space-separated)
names = input("Enter employee names (space-separated):").split()
print(names) #Enter employee names (space-separated): Ankit Ravi Sneha
             #Output: ['Ankit', 'Ravi', 'Sneha']
#Input as List (Comma-separated)
tags = input("Enter tags (comma-separated): ").split(',')
print(tags)  #Enter tags (comma-separated): sale,discount,new
             #Output: ['sale', 'discount', 'new']
#List of Integers
marks = list(map(int, input("Enter marks: ").split()))
print(marks)  #Enter marks: 89 76 94 82
              #Output: [89, 76, 94, 82]
#List of Floats
weights = list(map(float, input("Enter weights: ").split()))
print(weights)  #Enter weights: 55.6 62.1 70.3
                #Output: [55.6, 62.1, 70.3]
#Tuple Input
dimensions = tuple(map(int, input("Enter length, width,height: ").split()))
print(dimensions) #Enter length, width, height: 10 20 15
                  #Output: (10, 20, 15)
#Set Input
selected_ids = set(map(int, input("Enter selected image IDs:").split()))
print(selected_ids) #Enter selected image IDs: 101 102 103 101 104
                    #Output: {101, 102, 103, 104}
#Dictionary Input using eval()
profile = eval(input("Enter user profile as a dictionary: "))
print(profile) #Enter user profile as a dictionary: {'name': 'Ravi', 'age':30, 'role': 'admin'}
               #Output: {'name': 'Ravi', 'age': 30, 'role': 'admin'}
#Multiple Inputs with Unpacking
username, password = input("Enter username and password:").split()
print("Username:", username)
print("Password:", password)
#Enter username and password: user01 mypassword123
#Username: user01
#Password: mypassword123

#Only use eval() when input is trusted.