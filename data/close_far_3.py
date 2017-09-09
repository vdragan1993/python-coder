# print True if one of 5 and 3 is differing from 4 by at most 1, while the other is differing from both other values by 2 or more
a = 4
b = 5
c = 3
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
