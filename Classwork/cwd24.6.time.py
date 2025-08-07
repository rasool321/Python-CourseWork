from datetime import time
specific_time = time(14, 30, 15) # 14:30:15 (2:30:15 PM) #hours starts from 0 and ends with 23
print("Specific time:", specific_time)
print("Hour:", specific_time.hour) #14
print("Minute:", specific_time.minute)#30
print("Second:", specific_time.second)#15