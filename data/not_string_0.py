# print "not " added to the front if candy doesn't start with "not"
if 'candy'.startswith("not"):
    print('candy')
else:
    retVal = "not " + 'candy'
    print(retVal)
