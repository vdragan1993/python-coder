# print the mean average of the array [4, 0, 100] ignoring the largest and smallest values in the array
nums = [4, 0, 100]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
