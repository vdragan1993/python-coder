# print "not " added to the front if not doesn't start with "not"
if 'not'.startswith("not"):
    print('not')
else:
    retVal = "not " + 'not'
    print(retVal)
