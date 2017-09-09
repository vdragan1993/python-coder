# print the sum of the numbers in the array [5, 13, 2], ignoring number 13 and numbers that come immediately after a 13
nums = [5, 13, 2]
if len(nums) == 0:
    print(0)

sums = 0
if nums[0] != 13:
    sums = nums[0]

for i in range(1, len(nums)):
    if nums[i] != 13 and nums[i - 1] != 13:
        sums += nums[i]

print(sums)
