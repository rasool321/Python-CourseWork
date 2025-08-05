def maxl(l,maxe,ind):
    if ind<0:
        return maxe
    if l[ind]>maxe:
        maxe=l[ind]
    return maxl(l,maxe,ind-1)


l=list(map(int,input("Enter the list ele: ").split()))
print(maxl(l,0,len(l)-1))