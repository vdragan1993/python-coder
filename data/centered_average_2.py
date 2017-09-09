# print the mean average of the array [-10, -4, -2, -4, -2, 0] ignoring the largest and smallest values in the array
nums = [-10, -4, -2, -4, -2, 0]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
