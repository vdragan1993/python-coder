# print a new string where the first and last chars of hello have been exchanged
if len('hello') <= 1:
    print('hello')
else:
    first = 'hello'[0]
    last = 'hello'[len('hello')-1]
    retVal = ""
    for i in range(1, len('hello')-1):
        retVal += 'hello'[i]
    print(last + retVal + first)