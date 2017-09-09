# print a new string where the first and last chars of Chocolate have been exchanged
if len('Chocolate') <= 1:
    print('Chocolate')
else:
    first = 'Chocolate'[0]
    last = 'Chocolate'[len('Chocolate')-1]
    retVal = ""
    for i in range(1, len('Chocolate')-1):
        retVal += 'Chocolate'[i]
    print(last + retVal + first)