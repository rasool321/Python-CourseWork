#Printing Text
print("Hello, World!")#Output: Hello, World!
#Printing Multiple Items
name = "ras"
age = 21
print("Name:", name, "Age:", age) #Name: ras Age: 21
#Using sep to Change the Separator
print("2024", "02", "07", sep="-")#2024-02-07
#Using end to Control Line Endings
print("ras,", end=" ")
print("course!") #ras, course!
print("ras\ncourse") #ras
                    #course
print("Name:\tRas") #Name:   Ras
#Output Formatting
#1 Using Commas (Simple Print Method)
name = "ras"
age = 21
score = 95.5
# Using Commas
print("Name:", name, "Age:", age, "Score:", score) #Name: ras Age: 21 Score: 95.5
#Using Modulo Operator (% Formatting)
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))#Name: ras | Age:21 | Score: 95.50
# Using f-strings
print(f"Name: {name} | Age: {age} | Score: {score:.2f}") #Name: ras | Age: 21 | Score: 95.50
# Using str.format()
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score)) #Name: ras | Age: 21 | Score: 95.5