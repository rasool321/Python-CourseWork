def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Input
a, b = map(int, input("Enter two numbers separated by comma: ").split(','))
print("GCD:", gcd(a, b))
