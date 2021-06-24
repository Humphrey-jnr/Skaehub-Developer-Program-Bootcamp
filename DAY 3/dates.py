
import numpy as np
  
# for today
today = np.datetime64('today', 'D')
print("Today: ", today)
  
# for yesterday
yesterday = np.datetime64('today', 'D')
- np.timedelta64(1, 'D')
  
print("Yesterday: ", yesterday)
  
# for tomorrow
tomorrow = np.datetime64('today', 'D')
+ np.timedelta64(1, 'D')
  
print("Tomorrow: ", tomorrow)