year = int(input("Enter the year: "))
leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap_year(year))
