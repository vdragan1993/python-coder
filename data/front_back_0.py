# print a new string where the first and last chars of code have been exchanged
if len('code') <= 1:
    print('code')
else:
    first = 'code'[0]
    last = 'code'[len('code')-1]
    retVal = ""
    for i in range(1, len('code')-1):
        retVal += 'code'[i]
    print(last + retVal + first)