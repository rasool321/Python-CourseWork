s=input("Enter the string: ")
v='aeiouAEIOU'
le_s= lambda s: s[0] in v
print(le_s(s))