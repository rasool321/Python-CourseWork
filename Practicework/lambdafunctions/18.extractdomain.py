l=input("Enter the email address:")
domain = lambda s: s.split("@")[1]
print(domain(l))