def sumofl(l,ind):
    if ind>=len(l):
        return 0
    return l[ind]+sumofl(l,ind+1)
l=list(map(int,input("Enter the list ele:").split()))
print(sumofl(l,0))
