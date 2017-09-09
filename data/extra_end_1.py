# print a new string made of 3 copies of the last 2 chars of ab
s = 'ab'
if len(s) == 2:
    print(3*s)
else:
    substring = s[len(s)-2:]
    print(substring*3)
