# print a new string where the char at index 0 has been removed from Hi
retVal = ""
for i in range(0, len('Hi')):
    if i != 0:
        retVal += 'Hi'[i]
print(retVal)