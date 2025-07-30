def up_d(d, k, v):
    if k in d:
        d[k] = v
    else:
        d[k] = v
    return d

d = eval(input("Enter dictionary: "))  # Example: {'a': 1, 'b': 2}
k = input("Enter new key: ")
v = int(input("Enter the new value: "))
print("Updated dictionary:", up_d(d, k, v))
