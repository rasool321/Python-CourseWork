try:
    d={1:2,2:3,3:4}
    print(d[4])

except KeyError:
    print("key is not present(Keyvalue error)")