# print True if one of 3 and 5 is differing from 4 by at most 1, while the other is differing from both other values by 2 or more
a = 4
b = 3
c = 5
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
