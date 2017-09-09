# print the number of the positions where given strings  and hello contain the same length 2 substring
a = ''
b = 'hello'
if len(a) < 2 or len(b) < 2:
    print(0)
else:
    ret_val = 0
    for i in range(1, min(len(a), len(b))):
        if a[i-1] == b[i-1] and a[i] == b[i]:
            ret_val += 1

    print(ret_val)