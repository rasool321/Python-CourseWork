def even(n):
    print("Even numbers:",end=' ')
    for i in range(n+1):
        if i%2==0:
            print(i,end=' ')
n=int(input("Enter s number:"))
even(n)