import re
#re.match() "Checks if the pattern matches only at the start of the string."
result=re.match(r'[a-z]','hello world') 
o=re.match(r"\d",'12hello world')

print(result.group() if result else 'No Match')
print(o.group() if result else 'No Match')


#re.search() "Searches for the first occurrence of the pattern anywhere in the string."
r=re.search(r'[0-9]{2}','ds-da-14-15')
m=re.search(r'[a-z]*[0-9]$','hi234402')
x=re.search(r'h?i','hii')
print(r.group() if result else 'No Match')
print(m.group() if result else 'No Match')
print(x.group() if result else 'No Match')

#re.findall() 'Returns all matches in a list.'
a=re.findall(r'[0-9]{2}','da-ds-14-15')
print(a)
g=re.findall(r'h..','hot hit hat hee hii hurry')
print(g)
y=re.findall(r'\b\d{4}\b','34 56 32 534 23 42 22 34 3244 23 12 233423 23234 1234')
print(y)

#re.finditer() 'Returns an iterator of match objects.'
b=re.finditer(r'[0-9]{2}','pfs-30 & pfs-31 ds-da-14-15')
for i in b:
    print(i.group(),i.start())

#re.fullmatch() 'Checks if the entire string matches the pattern.'
c = re.fullmatch(r'[0-9]{2,8}', '34567890')
d = re.fullmatch(r'(aeiou)+', 'aeiou')
e= re.fullmatch(r'(aeiou)*', '')
f=re.fullmatch(r'^[6-9]\d{9}','9876542323')

print(c.group() if c else 'No Match')
print(d.group() if d else 'No Match')
print(e.group() if e else 'No Match')
print(f.group() if f else 'No Match')


#re.split() 'Splits a string at each match.'
text = "apple, banana; orange - grape"
t = re.split(r"[,; -]+", text)
print(t)

#re.sub() 'Replaces matches with another string.
k=re.sub(r'[aeiouAEIOU]','*0*','Python Programming Language')
l=re.sub(r'[A-Z]','-','Python Programming Language')
print(k)
print(l)