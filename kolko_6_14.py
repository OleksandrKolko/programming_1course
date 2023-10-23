# https://www.eolymp.com/uk/submissions/14842742
string = input()
string = string.replace(' ', '')
if string == string[::-1]:
    print('YES')
else:
    print('NO')