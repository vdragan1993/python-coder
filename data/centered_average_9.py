# print the mean average of the array [7, 7, 7] ignoring the largest and smallest values in the array
nums = [7, 7, 7]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
