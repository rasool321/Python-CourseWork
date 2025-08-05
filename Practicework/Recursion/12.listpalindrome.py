def pali(l,ind):
    if ind>=len(l):
        return True
    if l[ind]==l[len(l)-1-ind]:
        return True
    return pali(l,ind+1)
l=list(map(int,input("Enter the list ele:").split()))
print('Is Plindrome ',pali(l,0))