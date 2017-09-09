# print the number of even numbers in the [11, 9, 0, 1]
nums = [11, 9, 0, 1]
sol = 0
for num in nums:
    if num % 2 == 0:
        sol += 1

print(sol)
