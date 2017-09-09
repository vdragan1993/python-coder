# print the sum of the numbers in the array [1, 1, 6, 7, 2], ignoring sections of numbers starting with a 6 and extending to the next 7
nums = [1, 1, 6, 7, 2]
if len(nums) == 0:
    print(0)

sums = 0
started = 0
for num in nums:
    if started == 0:
        if num == 6:
            started += 1
        else:
            sums += num

    else:
        if num == 7:
            started -= 1

print(sums)
