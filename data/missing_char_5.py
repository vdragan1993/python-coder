# print a new string where the char at index 0 has been removed from code
retVal = ""
for i in range(0, len('code')):
    if i != 0:
        retVal += 'code'[i]
print(retVal)