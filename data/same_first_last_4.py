# print True if the array [] is length 1 or more, and the first element and the last element are equal
nums = []
if len(nums) > 0:
    if nums[0] == nums[len(nums)-1]:
        print('True')
    else:
        print('False')
else:
    print('False')
