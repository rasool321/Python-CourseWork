l=list(input("Enter the words: ").split())
sort_ele=sorted(l,key=lambda s : len(s))
print(sort_ele)