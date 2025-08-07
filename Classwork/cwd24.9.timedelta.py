from datetime import datetime,time,date,timedelta
today=date.today()
now = datetime.now()
# Adding 7 days
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date) #Date after 7 days: 2025-08-14
# Subtracting 3 days
past_date = today - timedelta(days=3)
print("Date 3 days ago:", past_date) #Date 3 days ago: 2025-08-04
# Adding 2 hours
future_time = now + timedelta(hours=2)
print("Time after 2 hours:", future_time) #Time after 2 hours: 2025-08-07 14:27:55.155786