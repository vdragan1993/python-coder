# print sum of 9, 2 and 2. However, if one of the values is the same as another, it does not count towards the sum
a = 9
b = 2
c = 2
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
