# print a new string where the first and last chars of aavJ have been exchanged
if len('aavJ') <= 1:
    print('aavJ')
else:
    first = 'aavJ'[0]
    last = 'aavJ'[len('aavJ')-1]
    retVal = ""
    for i in range(1, len('aavJ')-1):
        retVal += 'aavJ'[i]
    print(last + retVal + first)