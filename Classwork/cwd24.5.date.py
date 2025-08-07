from datetime import date

today=date.today()
print(today) #2025-08-07
print(today.year) #2025
print(today.month) #8
print(today.day) #7
print(today.weekday()) #3
#weeday 0-m,1-t,2-w,3-th,4-f,5-sa,6-s
print(today.isoweekday())
#weeday 1-m,2-t,3-w,4-th,5-f,6-sa,7-s
print(today.isocalendar()) #datetime.IsoCalendarDate(year=2025, week=32, weekday=4)

#specific date
specific_date = date(2024, 2, 16) 
print("Specific date:", specific_date) #Specific date: 2024-02-16