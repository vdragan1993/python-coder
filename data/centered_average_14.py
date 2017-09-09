# print the mean average of the array [6, 4, 8, 12, 3] ignoring the largest and smallest values in the array
nums = [6, 4, 8, 12, 3]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
