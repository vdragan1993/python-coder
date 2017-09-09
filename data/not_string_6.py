# print "not " added to the front if no doesn't start with "not"
if 'no'.startswith("not"):
    print('no')
else:
    retVal = "not " + 'no'
    print(retVal)
