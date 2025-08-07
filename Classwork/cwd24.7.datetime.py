from datetime import datetime
now = datetime.now()
print("Current date and time:", now) #Current date and time: 2025-08-07 12:16:26.750606

#create a specific date and time
specific_datetime = datetime(2024, 2, 16, 14, 30, 15)
print("Specific date and time:", specific_datetime)

#extracting the time and date componerts
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)