s = set()
print(s) #set()
{1, 2, 3} 
d= {1,2,3}
print(d,type(d)) #<class 'set'>
s = {1, 2, 2, 3, 4} #do not allow duplicates
print(s) #{1,2,3,4}

#operations in sets
#add
s.add(5) #only new ele is allow
s.add(1)
print(s) #{1, 2, 3, 4, 5}
#remove
s.remove(5)
print(s)  #{1, 2, 3, 4}
#membership
s = {1, 2, 3, 4}
print(3 in s) # Output: True
print(5 not in s) # Output: True

boys ={'rasool','varun','chaitu','tarit'}
girls = {'radha','sita','gita'}
online = {'praveen','tarit','madav','chaitu'}
#Union (| or union() method)
print(boys | girls) #{'chaitu', 'tarit', 'gita', 'sita', 'radha', 'rasool', 'varun'}
#Intersection (& or intersection() method)
print(boys & girls) # set()
print(boys & online) # {'tarit', 'chaitu'}
#Difference (- or difference() method)
#Returns elements in the first set but not in the second set.
print(boys-online) #{'varun', 'rasool'}
#Symmetric Difference (^ or symmetric_difference() method)
#Returns elements in either set1 or set2 but not both.
print(boys ^ girls) #{'gita', 'tarit', 'sita', 'radha', 'varun', 'chaitu', 'rasool'}
#Subset (<= or issubset() method)
a ={1,2,3}
# {},{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}
print({1} <= a) # <= or issubset() return True
print({1}.issubset(a) ) # <= or issubset() return True
print({4}.issubset(a) ) #False
#Superset (>= or issuperset() method)
print({1} >= a) #False
print({1,2,3} >= a) #True
print({1,2,3}.issuperset(a)) #True
#Disjoint Sets (isdisjoint() method)
print(boys.isdisjoint(girls)) #True
print(boys.isdisjoint(online)) #False

#Built-in methods
#add
boys.add('fas')
print(boys) #{'chaitu', 'tarit', 'rasool', 'fas', 'varun'}
#remove
boys.remove('fas')
print(boys) #{'varun', 'tarit', 'rasool', 'chaitu'}
#discord
#Removes an element; does not raise an error if the element doesn’t exist
boys.discard('das')
print(boys) #None
#pop Removes and returns an arbitrary or random ele
print(boys.pop()) #varun
#clear
boys.clear() 
print(boys) #set()
boys.update(('set2',2,'j'))
print(boys) #{'set2', 2, 'j'}

boys ={'rasool','varun','chaitu','tarit'}
online = {'praveen','tarit','madav','chaitu'}
#intersection_update(other_set)
#Updates the set with the intersection of itself and another set
boys.intersection_update(online)
print(boys) #{'chaitu', 'tarit'}
#difference_update (other_set)
#Updates the set by removing elements found in another set
boys ={'rasool','varun','chaitu','tarit'}
online = {'praveen','tarit','madav','chaitu'}
boys.difference_update(online)
print(boys) #{'rasool', 'varun'}
##symmetric_difference_update(other_set)
#Updates the set with the symmetric difference
boys ={'rasool','varun','chaitu','tarit'}
online = {'praveen','tarit','madav','chaitu'}
boys.symmetric_difference_update(online)
print(boys) #{'varun', 'madav', 'praveen', 'rasool'}

news = boys.copy()
print(boys) #{'praveen', 'varun', 'rasool', 'madav'}


#Built_in functions
print(len(boys)) #4
print(min(boys)) #chaitu
print(max(boys)) #varun
a = {1,2,3,5,4}
print(sum(a)) #15
print(sorted(boys)) #['chaitu', 'rasool', 'tarit', 'varun']
l = [1,2,4]
print(set(l)) #{1, 2, 4}

# Creating a frozenset
#dealing with the fixed data use frozen set
f = frozenset([1, 2, 3])
print(f)
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)
#f.add(4) #AttributeError: 'frozenset' object has no attribute 'add'
#we can perform the Built-in functions
print(len(f)) #3
print(min(f)) #1
print(max(f)) #3
print(sum(f)) #6
print(sorted(f)) #[1,2,3]