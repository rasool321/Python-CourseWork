import collections
w='Python program java program html file css file'.split() 
d=collections.Counter(w) #Counter({'program': 2, 'file': 2, 'Python': 1, 'java': 1, 'html': 1, 'css': 1})
print(d)