# print a new string where the first and last chars of a have been exchanged
if len('a') <= 1:
    print('a')
else:
    first = 'a'[0]
    last = 'a'[len('a')-1]
    retVal = ""
    for i in range(1, len('a')-1):
        retVal += 'a'[i]
    print(last + retVal + first)