# print a new string where the first and last chars of ab have been exchanged
if len('ab') <= 1:
    print('ab')
else:
    first = 'ab'[0]
    last = 'ab'[len('ab')-1]
    retVal = ""
    for i in range(1, len('ab')-1):
        retVal += 'ab'[i]
    print(last + retVal + first)