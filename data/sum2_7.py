# print sum of the first 2 elements in the [4]. If [4] length is less than 2, print sum of existing elements, print 0 if [4] lenth is 0
nums = [4]
if len(nums) == 0:
    print(0)
elif len(nums) == 1:
    print(nums[0])
else:
    print(nums[0] + nums[1])
