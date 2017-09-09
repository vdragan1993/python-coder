# print True if one of the first 4 elements in the given array [9, 2, 3] is 9
nums = [9, 2, 3]
if len(nums) < 4:
    print(9 in nums[:len(nums)])
else:
    print(9 in nums[:3])