#Empty List
l = [] # Empty list []
l1 = list() #[]
print(l,l1)

#List with Elements
l = [1, 2, 3, 4, 5] # List of integers
fruits = ["apple", "banana", "cherry"] # List of strings
n = [10, "Python", 3.14, True] # Mixed data types
print(l,fruits,n)

#List with Nested Lists
n_l = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(n_l)

#List using list() Constructor
t_l = list((1, 2, 3)) # Converting tuple to list
s_l = list("Python") # ['P', 'y', 't', 'h', 'o','n']
print(t_l,s_l)

#Accessing Elements in a List
print(l)
print(l[0]) # 1
print(l[1]) # 2
print(l[-1]) # 5 (Negative Indexing)
#slicing
print(l[1:4]) # [2,3,4]
print(l[:3]) # [1,2,3] (from start)
print(l[2:]) # [3,4,5] (to end)
print(l[-3:-1]) # [3,4]
print(l[::-1]) # [5,4,3,2,1] (Reverse list)
#changing ele
l = [10, 20, 30, 40]
l[2] = 100
print(l) # [10, 20, 100, 40]

#Adding Elements
l.append(50)# Append (adds to the end)
print(l)
l.insert(1, 15)# Insert (adds at a specific position)
print(l)#[10,15, 20, 100, 40]
l.extend([60, 70, 80])# Extend (adds multiple elements)
print(l) # [10, 15, 20, 100, 40, 50, 60, 70, 80]

#Removing Elements
l.remove(100) # Removes first occurrence of 100
print(l)#[10, 15, 20, 40, 50, 60, 70, 80]
l.pop(2) # Removes element at index 2
print(l)#[10, 15, 40, 50, 60, 70, 80]
l.pop() # Removes last element
print(l)#[10, 15, 40, 50, 60, 70]
del l[1] # Deletes element at index 1
print(l)#[10, 40, 50, 60, 70]
l.clear() # Clears the entire list
print(l)#[]

#List Methods
l = [10, 20, 30, 40,20]
print(l.count(20)) # 2
print(l.index(40)) # 3
l.sort()#sort
print(l) # [10, 20, 20, 30, 40]
l.reverse() #reverse
print(l) # [40,30,20,20,10]
l1 = l.copy() #copying
print(l1)#[40,30,20,20,10]

k = [20,10,30,40]
k.sort() #sorting
print(k) #[10, 20, 30, 40]
print(sorted(k)) #sorted  [10, 20, 30, 40]
print(len(k))#4
print(min(k))#10
print(max(k))#40
print(sum(k))#100
print(any(k)) #true , ele is present
print(all(k)) #true , ele is present