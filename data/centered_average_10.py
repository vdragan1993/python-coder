# print the mean average of the array [1, 7, 8] ignoring the largest and smallest values in the array
nums = [1, 7, 8]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
