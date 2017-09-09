# print a string of the form short + long + short, with the shorter string on the outside and the longer string on the inside, given two strings a=bb and b=a
a = 'bb'
b = 'a'
if len(a) > len(b):
    str_max = a
    str_min = b
else:
    str_max = b
    str_min = a

print(str_min + str_max + str_min)
