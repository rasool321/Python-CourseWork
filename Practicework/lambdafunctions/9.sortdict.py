d = eval(input("Enter name-age dict (e.g., {'Alice': 22, 'Bob': 18}): "))
sorted_age = sorted(d.items(), key=lambda item: item[1])  # item[1] is the age
print(sorted_age)
