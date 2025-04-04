# import time

# print(time.time)

# list = [ 1, 2, 3, 1]

# def sol(arg):
#     print(arg)
#     for number in arg:
#         print(number)
#         if number == 8:
#             return True
#         else:
#             continue
#     return False

# 

# dict = {}

# def contains_duplocate(arg):
#     for number in arg:
#         if number in dict:
#             dict[number] += 1
#         else:
#             dict[number] = 1

#     for k, v in dict.items():
#         if v > 1:
#             return True
#         else:
#             continue
#     return False
    

# print(contains_duplocate(list))

# def two_sum(arg, target):
#     for indx, val in enumerate(arg):
#         diff = target - val
#     print(diff)

# two_sum([2, 11, 7, 5], 9)

# import heapq

# numbers = [400, 200, 130, 100, 500]

# result = heapq.nlargest(3, numbers)

# print(result)


#### Map / Filter / Reduce

def cube(x):
    return x * x * x

print(cube(2))

# li = []
number = [ 2, 3, 4, 5, 6]
# for i in number:
#     li.append(cube(i))

li = list(map(cube, number))
print(li)

## filter

