# print "not " added to the front if is not doesn't start with "not"
if 'is not'.startswith("not"):
    print('is not')
else:
    retVal = "not " + 'is not'
    print(retVal)
