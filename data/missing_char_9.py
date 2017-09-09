# print a new string where the char at index 8 has been removed from chocolate
retVal = ""
for i in range(0, len('chocolate')):
    if i != 8:
        retVal += 'chocolate'[i]
print(retVal)