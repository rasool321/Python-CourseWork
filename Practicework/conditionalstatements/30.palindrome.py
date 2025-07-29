n = input("Enter the number:")
m = n[::-1]
if n == m:
    print(f"{n} is a palindrome..")
else:
    print(f"{n} is not a palindrome number..")