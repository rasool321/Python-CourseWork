def pali(s):
    c=s[::-1]
    return c==s
        
s=input("Enter a string: ")
print("Is palindrome:",pali(s))
