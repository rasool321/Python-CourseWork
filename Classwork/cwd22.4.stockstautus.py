stock = [True, False, True, False]
available=[index for index,j in enumerate(stock) if j==True]
print(available)