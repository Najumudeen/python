
# Brute Force Method O(n2)
# def twoSum(nums, target):
#     n = len(nums)

#     if n < 2:
#         return -1
    
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return[i, j]
            
#     return -1

# print(twoSum([1, 2, 5 ,3], 4))

# Two Pointer Method

def Solution(nums, target):
    prev_map = dict()

    for i, num in enumerate(nums):
        if target - num in prev_map:
            return [i, prev_map[target - num]]
        prev_map[num] = i
    return -1

print(Solution([1, 2, 5 ,3], 4))