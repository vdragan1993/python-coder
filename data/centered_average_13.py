# print the mean average of the array [4, 4, 4, 4, 5] ignoring the largest and smallest values in the array
nums = [4, 4, 4, 4, 5]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
