# Empty Tuple
empty_tuple = ()
# Single-element Tuple (note the trailing comma)
single_tuple = (5,)
# Multi-element Tuple
my_tuple = (1, "apple", 3.5)
# Without parentheses (implicit tuple creation)
implicit_tuple = 1, 2, 3
print(empty_tuple,single_tuple,my_tuple) # () (5,) (1, 'apple', 3.5)

#accessing tuple
t = (10, 20, 30, 40)
print(t[2]) # Output: 30
print(t[-1]) ## Output: 40

#Slicing
print(t[1:4])#(20, 30, 40)
print(t[-1:])#(40,)
print(t[:-1])#(10, 20, 30)
print(t[0:])#(10, 20, 30, 40)
print(t[:4])#(10, 20, 30, 40)

#Operations on Tuples
#concatination(+)
t1 = (1, 2)
t2 = (3, 4)
new_tuple = t1 + t2 # Output: (1, 2, 3, 4)
#repetation(*)
t=(1,2,'hi')
print(t*3)#(1, 2, 'hi', 1, 2, 'hi', 1, 2, 'hi')
#Membership Testing
t = (1, 2, 3)
print(2 in t) # Output: True
print(5 not in t) # Output: True
#unpacking
a, b, c = t
print(a, b, c) # Output: 1 2 3

#Built-in Functions for Tuples
print(len(t))#3
print(max(t))#3
print(min(t))#1
print(t.count(2))#1
print(t.index(2))#1
print(sum(t))#6
x = tuple([1, 2, 3]) #type converter
print(x) #(1, 2, 3

##
t_ch = (1, [2, 3])
t_ch[1][0] = 100
print(t_ch) # Output: (1, [100, 3])