# print a string of the form short + long + short, with the shorter string on the outside and the longer string on the inside, given two strings a=aaa and b=bb
a = 'aaa'
b = 'bb'
if len(a) > len(b):
    str_max = a
    str_min = b
else:
    str_max = b
    str_min = a

print(str_min + str_max + str_min)
