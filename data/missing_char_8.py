# print a new string where the char at index 3 has been removed from code
retVal = ""
for i in range(0, len('code')):
    if i != 3:
        retVal += 'code'[i]
print(retVal)