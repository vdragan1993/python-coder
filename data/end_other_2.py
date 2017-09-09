# print True if either of abc and abXabc appears at the very end of each other, ignoring upper/lower case differences
a = 'abc'
b = 'abXabc'
a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))
