# print True if 31 is within 2 of a multiple 10
a = 31
mod = a % 10
if mod <= 2 or mod >= 8:
    print('True')
else:
    print('False')
