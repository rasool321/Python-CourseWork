def numbers(n):
    if n==0:
        return n
    return n+(numbers(n-1))

n = int(input())
print(numbers(n))