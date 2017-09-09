# print True if arrays a=[1, 2, 3] and b=[7, 3, 2] have the same first element or they have the same last element
a = [1, 2, 3]
b = [7, 3, 2]
if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    print('True')
else:
    print('False')
