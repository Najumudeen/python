
## retry - parameterised
# import random
# import time


# def retry(retries=3, exception=Exception, delay=2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             attempts = 0
#             while attempts < retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except exception as e:
#                     attempts += 1
#                     print(f'Failed ({attempts}/{retries})')
#                     time.sleep(delay)
#             raise exception
#         return wrapper
#     return decorator


# @retry(retries=5, exception=ValueError, delay=2)
# def error_prone_function():
#     if random.random() < 0.9:
#         raise ValueError('Error!')
#     else:
#         print("Success")

# error_prone_function()


########################
# Type Check - Type enforcing decorator
#

# import random
# import time

# def type_check(*expected_types):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for arg, expected_type in zip(args, expected_types):
#                 if not isinstance(arg, expected_type):
#                     raise TypeError(f"Expected {expected_type} but got {type(arg)}")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


# @type_check(int, int)
# def add(a, b):
#     return a + b

# print(add(10, 20))



#################
# Debug Decorator
#


# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Result was {result}")
#         return result
#     return wrapper

# @debug
# def add(a, b):
#     return a + b

# print(add(10, 20))

#####################
# rate_limiter
# import time
# import random


# def rate_limiter(calls, period):
#     def decorator(func):
#         last_calls = []
#         def wrapper(*args, **kwargs):
#             nonlocal last_calls

#             now = time.time()

#             last_calls = [ call_time for call_time in last_calls if now - call_time < period ] # will give the call with last 5 seconds

#             if len(last_calls) > calls:
#                 raise RuntimeError("Raise limit exceeded. Try again later")

#             last_calls.append(now)

#             return func(*args, **kwargs)

#         return wrapper

#     return decorator

# @rate_limiter(calls=2, period=1)
# def fetch_data():
#     print('Fetching data ....')
#    # time.sleep(1)
#     time.sleep(0.1)
#     print("Received data!")



# fetch_data()
# fetch_data()
# fetch_data()
# fetch_data()
# fetch_data()

# list = [ "5", "3", "4", "3", "5", "4", "6", "8", "8"]

# list_new = {}
# for i in range(len(list)):
#     if list[i] in list_new:
#         list_new[list[i]] += 1
#     else:
#         list_new[list[i]] = 1

# #print(list_new)


# for k, v in list_new.items():
#     if v == 1:
#         print(k)

# res = 0
# for i in range(len(list)):
#     if res ^= list[i]:
#         return res

##################
# File handling

# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))

# file_path = os.path.join(script_dir, "test.json")

# with open(file_path, "r") as file:
#     data = file.read()
#     print(data)



# def contain_duplicate(n):
#     dict = {}
#     for i in range(len(n)):
#         if n[i] in dict:
#             dict[n[i]] += 1
#         else:
#             dict[n[i]] = 1
# #    return dict

#     for k, v in dict.items():
#         if v == 2:
#             return True
#     return  False

# def contain_duplicate(nums):
#     # unique_set = set()

#     # for num in nums:
#     #     if num in unique_set:
#     #         return True

#     #     unique_set.add(num)
#     # return False

#     return len(nums) > len(set(nums))

# n = [1 , 2, 3, 1]
# n = [1, 2, 3, 4]
# print(contain_duplicate(n))

# n = [1,2,3,4]

# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         print(n[i], n[j])


import requests

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r.status_code)
# print(r.ok)
# print(r.headers)
# print(r.headers)

#https://httpbin.org/

# payload = {'page': 2, 'count': 25}
# GET METHOD
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url) https://httpbin.org/get?page=2&count=25
# HTTP Methods
# Auth
# Status Code

#print(r.text)
# POST METHOD

# payload = {'username': 'USE_YOUR_USERNAME', 'password': 'USE_YOUR_PASSWORD'}
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)

# # Get json response

# r_dict = r.json()
# print(r_dict['form'])

# Form based authentication
# Basic Authentication


# print(r.json()) # it's a method use parameters ()

#print(r.content)

# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# #{
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "password": "XXXXXXXX",
#     "username": "XXXXXXXX"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "36",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.32.3",
#     "X-Amzn-Trace-Id": "Root=1-67e3f846-78dd47cc66341b531d740acb"
#   },
#   "json": null,
#   "origin": "49.207.55.14",
#   "url": "https://httpbin.org/post"
# }

# Basic Authentication request


# r = requests.get('https://httpbin.org/basic-auth/najumudeen/testing', auth=('USE_YOUR_USERNAME', 'USE_YOUR_PASSWORD'))

# print(r)

# ╰─ python3 python_decorators.py                                              ─╯
# {
#   "authenticated": true,
#   "user": "XXXXXXXXXX"
# }


# # Get json response

# r_dict = r.json()
# print(r_dict['form'])


# Timeoout

r = requests.get('https://httpbin.org/delay/1', timeout=3)

print(r)

# requests.exceptions.ReadTimeout%
