# print a new string composed of every substring of given string Bye
string = 'Bye'
ret_val = ''
for i in range(len(string)+1):
    ret_val += string[:i]

print(ret_val)