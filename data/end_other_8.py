# print True if either of yz and 12xz appears at the very end of each other, ignoring upper/lower case differences
a = 'yz'
b = '12xz'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
