# print a new string where the char at index 0 has been removed from kitten
retVal = ""
for i in range(0, len('kitten')):
    if i != 0:
        retVal += 'kitten'[i]
print(retVal)