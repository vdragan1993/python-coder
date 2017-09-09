# print the sum of the numbers in the array [], ignoring number 13 and numbers that come immediately after a 13
nums = []
if len(nums) == 0:
    print(0)

sums = 0
if nums[0] != 13:
    sums = nums[0]

for i in range(1, len(nums)):
    if nums[i] != 13 and nums[i - 1] != 13:
        sums += nums[i]

print(sums)
