# print the number of even numbers in the [1, 3, 5]
nums = [1, 3, 5]
sol = 0
for num in nums:
    if num % 2 == 0:
        sol += 1

print(sol)
