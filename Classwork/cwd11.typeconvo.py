#Converting from int
a = 10
print(type(a)) ##<class 'float'>
print(float(a)) #10.0
print(type(float(a))) #<class 'float'>
print(str(a)) #'10'
print(type(str(a)))#<class 'str'>
print(bool(a)) #True (Non-zero ints are True)
print(type(bool(a))) #<class 'bool'>
print(complex(a)) #(10+0j)
print(type(complex(a))) #<class 'complex'>
# int is a single value ...
#we can not convert single to multiple/iteratable vlaues like list,set,tuple,dict
#print(list(a)) #TypeError: 'int' object is not iterable
#print(type(list(a))) #TypeError: 'int' object is not iterable


#Converting from float
b = 10.0
print(type(b)) #<class 'float'>
print(int(b)) #10
print(type(int(b))) #<class 'int'>
print(str(b)) #'10.0'
print(type(str(b)))#<class 'str'>
print(bool(b)) #True (Non-zero floats are True)
print(type(bool(b))) #<class 'bool'>
print(complex(b)) #(10+0j)
print(type(complex(b))) #<class 'complex'>
# float is a single value ...
#we can not convert single to multiple/iteratable vlaues like list,set,tuple,dict
#print(list(b)) #TypeError: 'int' object is not iterable
#print(type(list(b))) #TypeError: 'int' object is not iterable


#Converting from str
s = 'rasool'
print(type(s)) #<class 'str'>
#if want to convert str in int or float the values should be in numeric ex: for int 1,2,3... for float 1.0,2.0,..
s='1'
print(int(s)) #1
print(type(int(s))) #<class 'int'>
s='1.0'
print(float(s)) #1.0
print(type(float(s))) #<class 'float'>
s='ras'
print(bool(s)) #True (Non-zero str are True)
print(type(bool(s))) #<class 'bool'>
s='ras'
print(list(s)) #['r', 'a', 's']
print(type(list(s))) #<class 'list'>
s='ras'
print(tuple(s)) #('r', 'a', 's')
print(type(tuple(s))) #<class 'tuple'>
s='ras'
print(set(s)) #{'a', 's', 'r'}
print(type(set(s))) #<class 'set'>
s='ras'
#print(dict(s))
#print(type(dict(s))) #Needs key-value pair structure

#Converting from list
l=[1,2,3,4]
print(type(l)) #<class 'list'>
#we can not convert multiple/iteratable to single vlaues like int,float,complex
#print(int(a)) #TypeError: 'int' object is not iterable
#print(type(int(a))) #TypeError: 'int' object is not iterable 
print(tuple(l)) #(1, 2, 3, 4)
print(type(tuple(l))) #<class 'tuple'>
print(bool(l)) #True (Non-zero str are True)
print(type(bool(l))) #<class 'bool'>
print(set(l)) #{1, 2, 3, 4}
print(type(set(l))) #<class 'set'>
#print(dict(l)) 
#print(type(dict(l))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#Converting from tuple
t=(1,2,3,4)
print(type(t))#<class 'List'>
print(list(t)) #[1, 2, 3, 4]
print(type(list(t))) #<class 'List'>
print(bool(t)) #True (Non-zero str are True)
print(type(bool(t))) #<class 'bool'>
print(set(t)) #{1, 2, 3, 4}
print(type(set(t))) #<class 'set'>
print(str(t)) #{1,2,3}
print(type(str(t))) #<class 'str'>
#print(dict(t)) 
#print(type(dict(t))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#Converting from set
n={1,2,3,4}
print(type(n))#<class 'set'>
print(list(n)) #[1, 2, 3, 4]
print(type(list(n))) #<class 'List'>
print(tuple(n)) #(1, 2, 3, 4)
print(type(tuple(n))) #<class 'tuple'>
print(str(n)) #{1 ,2,3,4}
print(type(str(n))) #<class 'str'>
#print(dict(n)) 
#print(type(dict(n))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#converting from dict
d = {1: 1, 2: 4, 3: 9}
print(type(d))#<class 'dict'>
print(list(d)) #[1, 2, 3]
print(type(list(d))) #<class 'List'>
print(tuple(d)) #(1, 2, 3)
print(type(tuple(d))) #<class 'tuple'>
print(set(d)) #{1, 2, 3}
print(type(set(d))) #<class 'set'>
print(bool(d)) #True
print(type(bool(d))) #<class 'bool'>
print(str(d)) #{1: 1, 2: 4, 3: 9}
print(type(str(d))) #<class 'str'>