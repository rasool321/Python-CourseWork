'''
#functional arguments and types ....
#1.positional argu
data=('xyz@gmail.com','xyz@123')
def login(mail,username,password):
    if mail==data[0] and password==data[1]:
        print(f'{username} - Login Successfull.')
    else:
        print(f'{username} - Invalid login')

mail = input("Enter the mail: ")
username = input("Enter the username : ")
password = input("Enter the password : ")
login(mail,username,password)

#2.keyword arg
data=('xyz@gmail.com','xyz@123')
def login(mail,user,passw):
    if mail==data[0] and password==data[1]:
        print(f'{username} - Login Successfull.')
    else:
        print(f'{username} - Invalid login')

mail = input("Enter the mail: ")
username = input("Enter the username : ")
password = input("Enter the password : ")
login(username=username,mail=mail,password=password)

#3.default arg
data=('xyz@gmail.com','xyz@123')
def login(username, password, mail='xyz@gmail.com'):
    if mail==data[0] and password==data[1]:
        print(f'{username} - Login Successfull.')
    else:
        print(f'{username} - Invalid login')

mail = input("Enter the mail: ")
username = input("Enter the username : ")
password = input("Enter the password : ")
login(username,password)
'''
#4.Variable-Length Arguments
#'*args' (Arbitrary Positional Arguments)
def add(*numbers):
    return numbers
print(add(1, 2, 3, 4, 5))#(1, 2, 3, 4, 5)


# 5. '**kwargs' (Arbitrary Keyword Arguments)
def display(**l):
    return l
print(display(py=289,spl=12123,htm=123))#{'py': 289, 'spl': 12123, 'htm': 123}
print(display(py=2,spl=3212,htm=13))#{'py': 2, 'spl': 3212, 'htm': 13}
print(display(py=12,spl=312,htm=1))#{'py': 12, 'spl': 312, 'htm': 1}
