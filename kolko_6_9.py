# https://www.eolymp.com/uk/submissions/14839643
string = input()
res = 0
operations = '*/-+%'
if '**' in string:
    res += string.count('**')
if '//' in string:
    res += string.count('//')
string = string.replace('**', '')
string = string.replace('//', '')
for op in operations:
    for i in string:
        if i == op:
            res += 1
print(res)