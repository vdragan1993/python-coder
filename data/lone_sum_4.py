# print sum of 2, 2 and 9. However, if one of the values is the same as another, it does not count towards the sum
a = 2
b = 2
c = 9
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
