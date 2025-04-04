values = []
for x in range(10):
    values.append(x)

# Using list comprehension
values = [ x for x in range(10) ]
print("1", values)

values = [ x + 1 for x in range(10) ]
print("2", values)

# Get all the even numbers from 0 - 50

evens = []

for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)

evens = [ numbers for numbers in range(50) if numbers % 2 == 0 ]

# Strings that start with "a" and end in "y"

options = ["any", "albany", "apple", "world", "hello"]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue

    if string[0] != "a":
        continue

    if string[-1] != "y":
        continue

    valid_strings.append(string)

print(valid_strings)

valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]

print(valid_strings)

# Multi List Comprehenstion

matrix = [[1,2,3], [4,5,6], [7,8,9]]

flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)

flattened = [ num for row in matrix for num in row ]

print(flattened)

# Categorize numbers as even or odd

categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

print(categories)

categories = [ 
    
    "Even" if x % 2 == 0 else "Odd" for x in range(10)
    
    ]
print(categories)

# Building a 3D list

import pprint

printer = pprint.PrettyPrinter()

#lst = []

# for a in range(5):
#     l1 = []
#     for b in range(5):
#         l2 = []
#         for num in range(5):
#             l2.append(num)
#         l1.append(l2)

#     lst.append(l1)

#printer.pprint(lst)

lst = [[ [num for num in range(5) ]for _ in range(5)]for _ in range(5)]

printer.pprint(lst)

# TRANSFORMATION IN COMPREHENSION

# LIST COMP with functions

def square(x):
    return x ** 2

square_numbers = [ square(x) for x in range(10) ]

print(square_numbers)

# Dictorary Comprehesion

# Creating a dictionary

pairs = [("a", 1), ("b", 2), ("c", 3)] # list of tuplies
my_dict = {k: square(v) for k,v in pairs}
print(my_dict)

# Set Comprehenstion

# Removing duplicates from a list while applying a function

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_squares = { x ** 2 for x in nums}

print(unique_squares)

# Generator Comprehenstion

sum_of_square = sum(x**2 for x in range(100000))