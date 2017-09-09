# print True if 6 appears as either the first or last element in the array [13, 6, 1, 2, 3]
nums = [13, 6, 1, 2, 3]
if len(nums) == 1:
    if nums[0] == 6:
        print('True')
    else:
        print('False')
else:
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        print('True')
    else:
        print('False')
