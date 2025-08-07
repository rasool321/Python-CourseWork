import collections
'''s='python program'
d=collections.defaultdict(int) #initialized every elem with 0
for i in s:
    d[i]+=1
print(d) #defaultdict(<class 'int'>, {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 1, ' ': 1, 'r': 2, 'g': 1, 'a': 1, 'm': 1})

s='python program'
d=collections.defaultdict(str)
for i in range(len(s)):
    d[i]+=s[i-1]
print(d)
'''
l=[1,2,3,4,4,5,1,2,3,2,4,2,1,3,4]
d=collections.defaultdict(int)
for i in l:
    d[i]+=1
print(d)
