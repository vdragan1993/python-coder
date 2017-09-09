# print "not " added to the front if bad doesn't start with "not"
if 'bad'.startswith("not"):
    print('bad')
else:
    retVal = "not " + 'bad'
    print(retVal)
