# print True if the array [1, 2, 3, 1] is length 1 or more, and the first element and the last element are equal
nums = [1, 2, 3, 1]
if len(nums) > 0:
    if nums[0] == nums[len(nums)-1]:
        print('True')
    else:
        print('False')
else:
    print('False')
