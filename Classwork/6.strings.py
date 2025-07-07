#Operations on Strings
# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Output: Hello World
# Repetition
print("rasool! " * 3) # Output: Python! Python! Python!
# Indexing
text = "rasool"
print(text[0]) # Output: r (1st character)
print(text[-1]) # Output: l (last character)
# Slicing
print(text[0:3]) # Output: ras (from index 0 to 2)
print(text[:4]) # Output: raso (default start is 0)
print(text[2:]) # Output: sool (from index 2 to end)
# Membership
print('ras' in text) # Output: True
print('Java' not in text) # Output: True


#Built-in String Functions
# 1. len()
text = "Hello World"
print(len(text)) # Output: 11
# 2. max() and min()
print(max(text)) # Output: 'r' (highest ASCII value)
print(min(text)) # Output: ' space ' (lowest ASCII value)
# 3. sorted()
print(sorted(text)) # Output: [' ', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
# 4. chr() and ord()
print(ord('A')) # Output: 65 (ASCII value of 'A')
print(chr(97)) # Output: 'a' (character for ASCII value 97)

#Case Conversion Methods
t='rasool'
print(t.upper()) #RASOOL
print(t.lower()) #rasool
s = 'rasool ba'
print(s.capitalize()) #Rasool ba
print(s.title()) #Rasool Ba
print(s.casefold()) #rasool ba

#Alignment & Formatting Methods
print(t.center(10, "*")) #**rasool**
print(t.ljust(10, "*")) #rasool****
print(t.rjust(10, "*"))#****rasool
print(t.zfill(10))#0000rasool

#Search & Find Methods
print(t.find("l"))#5
print(t.rfind("l"))#5
print(t.index("l"))#5
print(t.rindex("l"))#5
print(t.count("o"))#2

#String Testing Methods
print(t.startswith("r"))#True
print(t.endswith("l"))#True
print(t.isalpha())#True
print(t.isalnum())#True
print(t.islower())#True
print(t.isupper())#False
print(t.isspace())#False
print(t.istitle())#False
print(t.isidentifier())#True

#isdecimal() → Most strict; only base-10 digits ('0'–'9' and equivalents)
d = '123'
print(d.isdecimal())#True
d = '2'
print(d.isdecimal())#True

#isdigit() → Allows additional digit characters like superscripts
e = '123'
print(e.isdigit())#True
e = '2'
print(e.isdigit())#True

#isnumeric() → Most flexible; includes digits, fractions, Roman numerals, etc.
f= '123'
print(e.isnumeric())#True
f = '1⁄3'
print(e.isnumeric())#True

#Replace & Modify Methods
p='banana'
print(p.replace("b", "p"))#panana
print(p.translate(str.maketrans("a", "x")))#bxnxnx
print(p.maketrans("ana","%#5"))#{97: 53, 110: 35}

#Splitting & Joining Methods
print(p.split(","))#['banana']
print(p.rsplit(",",1))#['banana']
r='jai\nbahubali'
print(r.splitlines())#['jai', 'bahubali']
print(" ".join(["Hello", "World"]))#Hello World
print("apple-pie".partition("-"))#('apple', '-', 'pie')
print("apple-pie".rpartition("-"))#('apple', '-', 'pie')

#Whitespace & Trimming Methods
x = " ras "
print(x.strip())#ras
print(x.lstrip('-'))#--ras
print(x.rstrip('-'))#ras--

#Encoding & Decoding Methods
print("hello".encode("utf-8"))#b'hello'
print(b'hello'.decode("utf-8"))#hello