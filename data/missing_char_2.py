# print a new string where the char at index 4 has been removed from kitten
retVal = ""
for i in range(0, len('kitten')):
    if i != 4:
        retVal += 'kitten'[i]
print(retVal)