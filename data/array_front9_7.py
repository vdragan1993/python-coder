# print True if one of the first 4 elements in the given array [5, 5] is 9
nums = [5, 5]
if len(nums) < 4:
    print(9 in nums[:len(nums)])
else:
    print(9 in nums[:3])