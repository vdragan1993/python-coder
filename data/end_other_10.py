# print True if either of 12 and 12 appears at the very end of each other, ignoring upper/lower case differences
a = '12'
b = '12'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
