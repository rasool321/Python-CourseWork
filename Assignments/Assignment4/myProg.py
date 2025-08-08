import math

def replace_subinstr(string, old_sub, new_sub):
    return string.replace(old_sub, new_sub)

def replace_subinstr_demo():
    print("Program: Replace Substring")
    print('''\nCode:
def replace_subinstr(string, old_sub, new_sub):
    return string.replace(old_sub, new_sub)
''')
    print("Test Case 1: replace_subinstr('hello world', 'world', 'Python') → hello Python")
    print("Test Case 2: replace_subinstr('abcabc', 'a', 'z') → zbczbc")
    print("Explanation: Uses Python’s built-in `str.replace()` method to substitute one substring with another.")

def checkChar(c):
    if c.lower() in 'aeiou':
        return 'Vowel'
    return 'Consonant'

def checkChar_demo():
    print("Program: Check if Character is Vowel or Consonant")
    print('''\nCode:
def checkChar(c):
    if c.lower() in 'aeiou':
        return 'Vowel'
    return 'Consonant'
''')
    print("Test Case 1: checkChar('A') → Vowel")
    print("Test Case 2: checkChar('b') → Consonant")
    print("Explanation: Checks if character exists in vowel list using `in` and `lower()`.")

def lenofstr(s):
    return len(s)

def lenofstr_demo():
    print("Program: Find Length of a String")
    print('''\nCode:
def lenofstr(s):
    return len(s)
''')
    print("Test Case 1: lenofstr('hello') → 5")
    print("Test Case 2: lenofstr('Python') → 6")
    print("Explanation: Uses built-in `len()` function to count characters.")


def diamondPattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

def diamondPattern_demo():
    print("Program: Print Diamond Pattern")
    print('''\nCode:
def diamondPattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
''')
    print("Test Case: diamondPattern(3)")
    print("Explanation: First loop prints upper half, second loop prints lower half of diamond.")

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def pyramid_demo():
    print("Program: Print Pyramid Pattern")
    print('''\nCode:
def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
''')
    print("Test Case: pyramid(3)")
    print("Explanation: Creates symmetric triangle using nested loops and spacing.")


def floyd(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()

def floyd_demo():
    print("Program: Floyd’s Triangle")
    print('''\nCode:
def floyd(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()
''')
    print("Test Case: floyd(3)")
    print("Explanation: Prints triangle of numbers with increasing values in each row.")

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two Real and Distinct Roots:")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Two Real and Equal Roots:")
        print(f"Root = {root}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        print("Two Complex Roots:")
        print(f"Root 1 = {real} + {imag}i")
        print(f"Root 2 = {real} - {imag}i")

def find_roots_demo():
    print("📐 Program: Quadratic Equation Roots")
    print('''\nCode:
discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two Real and Distinct Roots:")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Two Real and Equal Roots:")
        print(f"Root = {root}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        print("Two Complex Roots:")
        print(f"Root 1 = {real} + {imag}i")
        print(f"Root 2 = {real} - {imag}i")
''')
    print("Test Case 1: a=1, b=-3, c=2 → Roots: 2, 1")
    print("Test Case 2: a=1, b=2, c=5 → Complex Roots")
    print("Explanation: Uses discriminant formula to determine root nature and value.")

def numberofdigit(n):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return 1 + numberofdigit(n // 10)

def numberofdigit_demo():
    print("Program: Count Digits using Recursion")
    print('''\nCode:
def numberofdigit(n):
    if n == 0:
        return 0
    return 1 + numberofdigit(n // 10)
''')
    print("Test Case 1: numberofdigit(123) → 3")
    print("Test Case 2: numberofdigit(10000) → 5")
    print("Explanation: Recursively counts digits by dividing number by 10 each time.")


# 9. Sum of n Natural Numbers
def sumofn(n):
    return n * (n + 1) // 2

def sumofn_demo():
    print("Program: Sum of First n Natural Numbers")
    print('''\nCode:
def sumofn(n):
    return n * (n + 1) // 2
''')
    print("Test Case 1: sumofn(5) → 15")
    print("Test Case 2: sumofn(100) → 5050")
    print("Explanation: Uses formula `n(n+1)/2` for efficient computation.")

def is_perfect(n):
    if n <= 0:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

def is_perfect_demo():
    print("✨ Program: Check Perfect Number")
    print('''\nCode:
def is_perfect(n):
    if n <= 0:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n
''')
    print("Test Case 1: is_perfect(28) → True")
    print("Test Case 2: is_perfect(10) → False")
    print("Explanation: A perfect number is one whose sum of divisors equals the number itself.")
