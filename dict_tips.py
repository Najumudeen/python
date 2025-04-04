# #Question1:
#
# data = {}
# print(type(data))
#
# # Set Create in Python
#
# data = set()
# print(type(data))
#
# # Question 2
#
# print(-10//3)
#
# # print(
# # "\"\"\"
# # Conversion - He Said, "Shantanu's
# # \"\"\"")
#
# name = "shantanu"
# print(name[2:8:2])
#
# my_dict = {"jay":89, "viru":81, "jay": 52}
# print(len(my_dict)
#       )
# print(my_dict["jay"])
#
#
# a = [1, 4, 7]
# b = [2, 5, 8]
# c = [3, 6, 9]
# print(a + b + c)
# print(zip(a, b, c))
# print(list(zip(a,b,c)))
#
#
# print(10.0//3)
# #
# # for i in 765<1:
# #     print(i)
#

# Generator


def pattern(arg):
      dict = {}
      for i in arg.split(','):
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
      return dict

a = pattern("a,a,a,b,b,c,c,c")

print(a)


def splitandmergerfunc(arg):
      val = arg.split()
      new_val = val[::-1]
      final_value = ' '.join(new_val)
      return final_value

b = splitandmergerfunc("Sky is blue")

print(b)
