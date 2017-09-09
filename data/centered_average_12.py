# print the mean average of the array [1000, 0, 1, 99] ignoring the largest and smallest values in the array
nums = [1000, 0, 1, 99]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
