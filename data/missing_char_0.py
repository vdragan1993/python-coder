# print a new string where the char at index 1 has been removed from kitten
retVal = ""
for i in range(0, len('kitten')):
    if i != 1:
        retVal += 'kitten'[i]
print(retVal)