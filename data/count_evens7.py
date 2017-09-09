# print the number of even numbers in the [2, 5, 12]
nums = [2, 5, 12]
sol = 0
for num in nums:
    if num % 2 == 0:
        sol += 1

print(sol)
