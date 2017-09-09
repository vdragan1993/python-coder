# print True if either of ab and ab12 appears at the very end of each other, ignoring upper/lower case differences
a = 'ab'
b = 'ab12'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
