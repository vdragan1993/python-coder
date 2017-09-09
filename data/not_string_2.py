# print "not " added to the front if not bad doesn't start with "not"
if 'not bad'.startswith("not"):
    print('not bad')
else:
    retVal = "not " + 'not bad'
    print(retVal)
