# print True if 22 is within 2 of a multiple 10
a = 22
mod = a % 10
if mod <= 2 or mod >= 8:
    print('True')
else:
    print('False')
