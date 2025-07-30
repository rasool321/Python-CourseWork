l=list(input("Enter the ele: ").split())
fil_ele=list(filter(lambda i : len(i)>3, l))
print(fil_ele)