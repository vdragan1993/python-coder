# print a new string composed of every substring of given string Bad
string = 'Bad'
ret_val = ''
for i in range(len(string)+1):
    ret_val += string[:i]

print(ret_val)