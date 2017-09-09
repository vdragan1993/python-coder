# print True if either of ab and 12ab appears at the very end of each other, ignoring upper/lower case differences
a = 'ab'
b = '12ab'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
