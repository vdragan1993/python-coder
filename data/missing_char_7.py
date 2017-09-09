# print a new string where the char at index 2 has been removed from code
retVal = ""
for i in range(0, len('code')):
    if i != 2:
        retVal += 'code'[i]
print(retVal)