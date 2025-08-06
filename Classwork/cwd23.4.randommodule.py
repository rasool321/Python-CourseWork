import random
#random.seed(5) #seed uses for constant random values..
print(random.random())
print(random.randint(1,5))
print(random.uniform(1,5)) #random float values in this range
name=['luffy','zoro','nami','sanjii','franki','robin','jimbe','loki']
print(random.choice(name))
print(random.choices(name,k=2)) #k returns 2 values random
print(random.shuffle(name),name) #shuffles the list
