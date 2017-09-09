# print the count of the number of times that a substring length 2 appears in the given string  and also as the last 2 chars of the string
string = ''
if len(string) < 2:
    print(0)

ret_val = 0
substring = string[len(string)-2:]

for i in range(1, len(string)):
    if substring[0] == string[i-1] and substring[1] == string[i]:
        ret_val += 1

print(ret_val-1)