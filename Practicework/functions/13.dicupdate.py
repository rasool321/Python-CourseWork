def up_d(d, k, v):
    if k in d:
        d[k] = v
    else:
        print("Key not found! Adding it.")
        d[k] = v
    return d

d = eval(input("Enter dictionary: "))  # Example: {'a': 1, 'b': 2}
k = input("Enter key to update: ")
v = int(input("Enter the value: "))
print("Updated dictionary:", up_d(d, k, v))
