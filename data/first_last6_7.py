# print True if 6 appears as either the first or last element in the array [6]
nums = [6]
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
