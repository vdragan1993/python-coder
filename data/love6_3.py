# print True if either of a = 1 and b = 6 is 6, or if their sum or difference is 6
a = 1
b = 6
if a == 6 or b == 6 or a + b == 6 or abs(a-b) == 6:
    print('True')
else:
    print('False')
