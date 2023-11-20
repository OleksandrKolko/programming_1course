# https://www.eolymp.com/uk/problems/8994
a = input()
b = input()
bool = True
for el in b:
    if el not in a:
        print('No')
        bool = False
        break
if bool:
    print('Ok')