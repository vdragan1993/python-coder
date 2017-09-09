# print the mean average of the array [1, 1, 5, 5, 10, 8, 7] ignoring the largest and smallest values in the array
nums = [1, 1, 5, 5, 10, 8, 7]
this_sum = sum(nums) - max(nums) - min(nums)
print(this_sum / (len(nums) - 2))
