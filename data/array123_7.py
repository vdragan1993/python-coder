# print True if the sequence 1, 2, 3 appears in the given array [1, 2]
nums = [1, 2]
if len(nums) < 3:
    print(False)
else:
    for i in range(2, len(nums)):
        if nums[i-2] == 1 and nums[i-1] == 2 and nums[i] == 3:
            print(True)

print(False)