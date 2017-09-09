# print True if either of Hiabc and bc appears at the very end of each other, ignoring upper/lower case differences
a = 'Hiabc'
b = 'bc'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
