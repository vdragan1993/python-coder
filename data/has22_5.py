# print True if the array [1, 3, 2, 2] contains a 2 next to a 2 somewhere
nums = [1, 3, 2, 2]
printed = False
for i in range(1, len(nums)):
    if nums[i] == 2 and nums[i - 1] == 2:
        print('True')
        printed = True

if not printed:
    print('False')
