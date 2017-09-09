# print True if one of 10 and 8 is differing from 10 by at most 1, while the other is differing from both other values by 2 or more
a = 10
b = 10
c = 8
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
