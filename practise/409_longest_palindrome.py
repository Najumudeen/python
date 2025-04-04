

# def longestPalindrome(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1


#     # print(char_count)
#     # for char in char_count:
#     #     print(char)
#     #     print("CHAR", char_count[char])
#     final_count = 0
#     #odd_is_present = False

#     for char in char_count:
#         if char_count[char] % 2 == 0:
#             final_count += char_count[char]
#         # else:
#         #     odd_is_present = True

#     final_count += 1

#     return final_count
    

# s = "abccccdd"
# #s = "a"

# print(longestPalindrome(s))

tuple1 = ("max",)
print(type(tuple1))

# build in tuple function
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

print(mytuple[-1])

for i in mytuple:
    print(i)

# check element in the tuple

if "Max" in mytuple:
    print("yes")
else:
    print("no")

# no of element in the tuple
print(len(mytuple))

# count no of element in the loop
print(mytuple.count("Max"))

# Get the index of the element
print(mytuple.index("Max"))

# convert tuple to list
my_list = list(mytuple)
print(my_list)

# Slicing with tuple

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
c = a[:5]

print(b)
print(c)

# Unpacking
my_tuple = "Max", 20, "Boston"
print(type(my_tuple))

name, *age = my_tuple

print(name)
print(age)

#####
# String

my_string = "Hello World"
print(my_string)

char = my_string[::2]
print(char)

greeting = "Hello"
for i in greeting:
    print(i)

if 'e' in greeting:
    print("yes")

my_string = '     Hello World     '
my_string = my_string.strip()
print(my_string)

my_string = 'Hello World'
# my_string = my_string.upper()
# print(my_string)
# my_string = my_string.lower()
# print(my_string)
# my_string = my_string.startswith('Hello')
# #print(my_string)

#print(my_string.endswith('World'))

print(my_string.count('o'))
print(my_string.replace('world', 'Universe'))

## List and strings
# convert string to list
my_string = 'how are you doing'
my_list = my_string.split(" ") # delimeter space
print(my_list)