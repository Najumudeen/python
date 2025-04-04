# import json 
# import requests
# API_KEY = "USE_YOUR_OWN_KEY"
# city_name = input("Enter your citi name: ")
# URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
# r = requests.get(URL)
# print(r.json())
# # data = json.loads(r.text)
# print(data)

########################################3

import psutil

# CPU times
print(psutil.cpu_times())

# Avg CPU load
print(psutil.getloadavg())

# Memory
print(psutil.virtual_memory())

# Swap Memory
print(psutil.swap_memory())

# Disk usage
print(psutil.disk_usage('/'))


# Disk IO utilization
print(psutil.disk_io_counters(perdisk=False))

# Teamp
#print(psutil.sensors_temperatures())
