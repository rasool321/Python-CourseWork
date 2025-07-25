#Scope of Variables
#1.Local Scope
'''
def greet():
    message = "Hello" #local scope..
    print(message)
greet()
#print(message) # Error(Name Error): message is not defined outside

#2.Global Scope

message = "Hello" #Global scope..
def greet():
    print(message) #Hello
greet() #Hello
print(message) # Hello
# or using global keyword
def greet():
    global message  #global keyword
    message = "Hello"#local scope..
    print(message)
greet()
print(message)

#Enclosing Scope (Nonlocal Scope)
#Nonlocal 
def outfun():
    course='py'
    print('First selected course:',course)
    def innerfunc():
        nonlocal course #To overwrite the inside func local scope use the 'nonlocal' keyword for making it global..
        course = 'java' 
        print('Student Modified:',course) #java  
    innerfunc()
    print('Final selected:',course) #py , if nonlocalthere 'java'
outfun()
#print('Outside func: ',course)
'''

#4.built-in scope
l=[1,2,3,4]
#sum=0 #overriding , not delcare them cause they are already a global scope
print(sum(l))  #10