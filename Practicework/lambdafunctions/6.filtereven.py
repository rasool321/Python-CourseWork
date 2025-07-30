l=list(map(int,input("Enter the list item:").split()))
e=list(filter(lambda i: i%2==0 , l))
print(e)