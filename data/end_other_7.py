# print True if either of xyz and 12xyz appears at the very end of each other, ignoring upper/lower case differences
a = 'xyz'
b = '12xyz'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
