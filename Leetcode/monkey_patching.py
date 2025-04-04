# ## Newton School Online Python training

# class Test:

#     def __init__(self, x):
#         self.x = x
    
#     def get_data(self):
#         print("some code to fetch data from database")

    
#     def f1(self):
#         self.get_data()
    
#     def f2(self):
#         self.get_data()

#     def new_get_data(self):
#         print("Some code to fetcg data from test data")
   
# t1 = Test(5)

# # t1.f1()
# # t1.f2()

# Test.get_data = new_get_data
# print("After Monkey Patching")

# t1.f1()
# t1.f2()

import A

def cube(self, num):
    return f"Cube of the number is: {num ** 3}"


# Monkey Patching

#A.Power.square = cube
 
obj = A.Power()

print(obj.square(3))