lst = [1, 2, 3, 4]
result = list(map(lambda x: x[0] * x[1], enumerate(lst)))
print(result)  