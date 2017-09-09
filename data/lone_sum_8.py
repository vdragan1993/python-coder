# print sum of 1, 3 and 1. However, if one of the values is the same as another, it does not count towards the sum
a = 1
b = 3
c = 1
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
