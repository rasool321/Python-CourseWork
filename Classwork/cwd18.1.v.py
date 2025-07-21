n = int(input("Enter the value of n: "))
for i in range(n):
    for j in range(n):
        if (j == 0 or j == n - 1) and i <= n // 2 or (i - j == n // 2 and i >= n // 2) or (i + j == n-1 + n // 2 and i >= n // 2):
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print()
