# print the mean average of the array [0, 2, 3, 4, 100] ignoring the largest and smallest values in the array
nums = [0, 2, 3, 4, 100]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
