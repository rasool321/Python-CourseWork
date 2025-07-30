def fibi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n0 = 0
        n1 = 1
        for i in range(2, n + 1):
            f = n0 + n1
            n0 = n1
            n1 = f
        return f


n=int(input("Enter the term number: "))
print(f'Fibonacci number is: {fibi(n)}')