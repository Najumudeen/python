# import time
# from functools import cache

# @cache
# def process_input(n):
#     # do some calculations
#     time.sleep(2)
#     return n ** 2

# print(process_input(5))
# print(process_input(5))
# print(process_input(5))
# print(process_input(5))
# print(process_input(5))

# Avoid Duplicate code
########################

# import time

# def time_logger(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f'Time Taken: {end - start:.4f}')
#         return result
#     return wrapper

# @time_logger
# def process_input(n):
#     time.sleep(2)
#     return n**2

# print(process_input(5))

#######
# 

import random
import time

def error_prone_function():
    if random.random() < 0.9:
        raise ValueError('Error!')
    else:
        print("Success")


