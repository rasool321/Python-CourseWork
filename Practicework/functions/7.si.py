def si(p,t,r):
    c=(p*t*r)/100
    return round(c,2)

p,t,r=input("Enter Principal, Rate, and Time:").split()
print(si(int(p),int(t),int(r)))