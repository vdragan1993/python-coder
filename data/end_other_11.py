# print True if either of abcXYZ and abcDEF appears at the very end of each other, ignoring upper/lower case differences
a = 'abcXYZ'
b = 'abcDEF'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
