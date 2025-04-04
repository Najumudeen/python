
# def Foo(n): 
#     def multiplier(x): 
#         return x * n 
#     return multiplier 

# a = Foo(5) 
# b = Foo(5) 
# print(a(b(2)))

# Overall explanation
# Here, `a` and `b` are multiplier functions that take `x` and multiply it by `5`. When we call `a(b(2))`, it's equivalent to `5 * (5 * 2)`, which equals `100`.

# class A:
#     def __init__(self, i = 0):
#     self.i = i 
# class B(A): 
#     def __init__(self, j = 0): 
#         self.j = j 
#     def main(): 
#         b = B() 
#         print(b.i) 
#         print(b.j) 
#     main() 



def checkIfExist(arr):
    seen = set()
    for a in arr:
        if a * 2 in seen or a % 2 == 0 and a // 2 in seen:
            return True
        seen.add(a)

    return False


#arr = [10,2,5,3]
arr = [3,1,7,11]

print(checkIfExist(arr))

