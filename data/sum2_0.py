# print sum of the first 2 elements in the [1, 2, 3]. If [1, 2, 3] length is less than 2, print sum of existing elements, print 0 if [1, 2, 3] lenth is 0
nums = [1, 2, 3]
if len(nums) == 0:
    print(0)
elif len(nums) == 1:
    print(nums[0])
else:
    print(nums[0] + nums[1])
