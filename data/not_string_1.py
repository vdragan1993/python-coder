# print "not " added to the front if x doesn't start with "not"
if 'x'.startswith("not"):
    print('x')
else:
    retVal = "not " + 'x'
    print(retVal)
