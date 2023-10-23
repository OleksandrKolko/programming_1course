# https://www.eolymp.com/uk/submissions/14839808
string = input()
res_str = ''
for i in string:
    if i >= 'A':
        res_str += i * 2
    else:
        res_str += i
print(res_str)