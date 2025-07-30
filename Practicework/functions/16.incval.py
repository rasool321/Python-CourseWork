def up_d(d):
    for i in d:
        d[i] = d[i]+1
    return d

d = eval(input("Enter dictionary: "))  
print("Updated dictionary:", up_d(d))
