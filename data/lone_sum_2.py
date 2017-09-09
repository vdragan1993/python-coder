# print sum of 3, 3 and 3. However, if one of the values is the same as another, it does not count towards the sum
a = 3
b = 3
c = 3
if a == b == c:
    print(0)
elif a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(a + b + c)
