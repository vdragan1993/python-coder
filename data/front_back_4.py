# print a new string where the first and last chars of  have been exchanged
if len('') <= 1:
    print('')
else:
    first = ''[0]
    last = ''[len('')-1]
    retVal = ""
    for i in range(1, len('')-1):
        retVal += ''[i]
    print(last + retVal + first)