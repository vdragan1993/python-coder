# print the mean average of the array [100, 0, 5, 3, 4] ignoring the largest and smallest values in the array
nums = [100, 0, 5, 3, 4]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
