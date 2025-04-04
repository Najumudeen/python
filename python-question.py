print(8 // 3)

# strip() method Trims leading and trailing spaces
example = ",Python,,"
print(example.strip(','))

# type() method
var = "123"
print(type(var))

# insert() an item at a specific index in a list in python

list = [ 1, 2, 4]
list.insert(2, 3)
print(list)

# while loop
# The while True: loop will continue indefinitely because the condition True is always true.”

#while True: print("Hello")
#while False: print("Hello")

x = ["apple", "banana", "cherry"]
y = x
print(y)
y[1] = "kiwi"
print(x)
print(y)

x = [ 1,2,3 ]
y = x
x.append(4)
print(y)
#NOTE: Lists in Python are mutable and assigning y = x does not create a copy but rather a reference. Changing y ia ALSO changes x

# pass statement is used inPython as a place holder for future code

# Non-empty string in Python are considered truthy values

# readline() function reads a single line from the file where the file pointer is current located and moves the file pointer

# used to combine two lists in python
# extend()

# enumerate() function return
# A list of tuples

nums = [ 1, 2, 3, 4]
nums = nums * 2 # nums *= 2
print(nums)

# Generate random numbers? random modules
#
import functools
@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))

# Break Teminates the loop immediately
for i in range(5):
    if i == 3:
        break
    print(i)

a = [1, 2, 3]
b = a
b.append(4)
print(a)

# Tuple, A tuple is a collection which is ordered and immutable, meaning that it's cpntent can not be changed once it is created


print("Python3.8".isdigit())

# String Method

import string
import random

char_pool = string.ascii_letters + string.ascii_uppercase + string.digits

print(''.join(random.sample(char_pool, 6))
