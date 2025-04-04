import re

# print(re.search(r'[\d]+', '6th Floor, A-118, \
# Sector-136, Noida, Uttar Pradesh - 201305'))


# grp = re.search(r'(?P<dd>[\d]{2})-([\d]{2})-([\d]{4})', '26-08-2029')

# print(grp.group('dd'))

import sys, os

# n = len(sys.argv)
# print("Total arguments passed:", n)


# print("\nName of Python script:", sys.argv[0])

# print("\nArguments passed:", end = " ")

# for i in range(1, n):
#     print(sys.argv[i], end = " ")


# print(dir(sys))

# print(dir(os.utime))
# cars = "test"
# print(len(cars))

#cars = ["Ford", "Volvo", "BMW"]

# cars = ["Ford", "Volvo", "BMW"]

# cars = [ 1, 2, 3, 4]
# print(cars)

# # #cars.remove("BMW")
# # #cars.reverse()
# # cars.insert(3, "MG")

# # print(cars)

# list = list(map(lambda x : x + 2, cars))
# print(list)  


# class geeks:

#     counter = 0
#     # constructor of geeks class

#     def __init__(self):
        
#         # increment
#         geeks.counter += 1


# # object or instance of geeks class

# g1 = geeks()
# # g2 = geeks()
# # g3 = geeks()

# print(geeks.counter)

# Python Program to find second largest element in an array

# using Sorting

def getSecondLarget(arr):

    print(arr)

    n = len(arr)

    print(n)

    # Sort the array in non-decreasing order
    arr.sort()
    print(arr)
    
    # start from second last element as last element is the largest
    for i in range(n - 2, -1, -1):

        # return the firsr element which is not equal to the 
        # larget element

        if arr[i] != arr[n - 1]:
            return arr[i]
    
    # if no second larget element was found, return -1
    return -1


a = [12, 35, 1, 33, 10, 1, 35, 31, 36]

print(getSecondLarget(a))a