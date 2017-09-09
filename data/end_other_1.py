# print True if either of AbC and HiaBc appears at the very end of each other, ignoring upper/lower case differences
a = 'AbC'
b = 'HiaBc'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
