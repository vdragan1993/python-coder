# given a string Hello, print a new string made of every other char starting with the first
string = 'Hello'
if len(string) > 0:
    ret_val = string[0]
    for i in range(1, len(string)):
        if i % 2 == 0:
            ret_val += string[i]
else:
    ret_val = ""

print(ret_val)