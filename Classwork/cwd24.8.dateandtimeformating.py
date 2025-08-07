from datetime import datetime,time,date,timedelta
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
formatted_datetime = now.strftime("%d-%B-%Y %I:%M %p")
print("Formatted Date:", formatted_date)#Formatted Date: 2025-08-07
print("Formatted Time:", formatted_time)#Formatted Time: 12:22:40
print("Formatted Date and Time:", formatted_datetime)#Formatted Date and Time: 07-August-2025 12:22 PM