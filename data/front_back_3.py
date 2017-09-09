# print a new string where the first and last chars of abc have been exchanged
if len('abc') <= 1:
    print('abc')
else:
    first = 'abc'[0]
    last = 'abc'[len('abc')-1]
    retVal = ""
    for i in range(1, len('abc')-1):
        retVal += 'abc'[i]
    print(last + retVal + first)