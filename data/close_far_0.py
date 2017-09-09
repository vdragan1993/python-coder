# print True if one of 2 and 10 is differing from 1 by at most 1, while the other is differing from both other values by 2 or more
a = 1
b = 2
c = 10
if abs(a - b) <= 1:
    if abs(a - c) >= 2 and abs(b - c) >= 2:
        print('True')
    else:
        print('False')
elif abs(a - c) <= 1:
    if abs(a - b) >= 2 and abs(b - c) >= 2:
        print('True')
    else:
        print('False')
