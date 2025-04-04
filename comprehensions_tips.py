
####################
# Example 1

# values = []
# for i in range(10):
#     values.append(i)
# print(values)

# Using list comprehension

# values = [ x + 1 for x in range(10) ]
# print(values)


####################
# Example 2

# Get all the even numbers from 0- 50
# evens = []

# for number in range(50):
#     is_even = number % 2 == 0
#     if number == 0:
#         continue
#     elif is_even:
#         evens.append(number)
# print(evens)
    
# evens = [ number for number in range(50) if number % 2 == 0 ]
# print(evens)

####################
# 

#Strings that start with "a" and end in "y"

#options = ["any", "albany", "apple", "world", "hello", "acy"]

# valid_strings = []

# for string in options:
#     if len(string) <= 1:
#         continue
#     elif string[0] != "a":
#         continue
#     elif string[-1] != "y":
#         continue
#     else:
#         valid_strings.append(string)

# print(valid_strings)

# valid_string = [
#     string
#     for string in options
#     if len(string) >= 2
#     if string[0] == "a"
#     if string[-1] == "y"
# ]
# print(valid_string)

####################
# Nested List 

# Flattening a mstrix (list of lists) 2 Dimenstion 

# matrix = [[1,2,3], [4,5,6], [7,8,9], "naju"]
# flattened = []

# for row in matrix:
#     for num in row:
#         flattened.append(num)

# print(flattened)


# flattened = [ num for row in matrix for num in row ]

# print(flattened)

####################
# Single Number

value = [3, 4, 2, 4, 2 ]

# dict = {}

# for i in value:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# for k, v in dict.items():
#     if v == 1:
#         print(k)

# res = 0
# for i in value:
#     res = res ^ i
# print(res)

####################
# Lambda function

# def add(x,y):
#     return x + y

# Change the above function to lambda function
# Lambda function donn't requirted return keyword
# add = lambda x, y: x + y

# print(add(5, 7))

# print((lambda x, y: x + y)(5,7))

# define a function make it list comprehention

# def double(x):
#     return x * 2

# sequence = [ 1, 3, 5, 9 ]
# doubled = [ double(x) for x in sequence ]
# doubled = [ double(x) for x in sequence ]
# # We can use map function

# doubled = map(double, sequence)

# # if want to use lambda function
# doubled = list(map(lambda x: x * 2, sequence))

# print(doubled)

####################
# Dictionary Comprehention

# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234")
# ]

# username_mapping = { user[1]: user for user in users }

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# _, username, password = username_mapping[username_input]

# # print(_)
# # print(username)
# # print(password)

# if password_input == password:
#     print("Your details are correct!.")
# else:
#     print("Your details are incorrect.")
    

####################
# Unpacking Arguments


def multiply(*args):
    print(args)
    total = 1  
    for arg in args:
        total *= arg
    return total

print(multiply(1, 3, 5))

def add(x, y):
    return x + y

#nums = [ 3, 5, 6 ]
nums = { "x": 15, "y": 25 }
add(**nums)

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"
    
print(apply(1, 3, 6, 7, operator="*"))




####################
#

####################
#
