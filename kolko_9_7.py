# https://www.eolymp.com/uk/submissions/15155694
n = int(input())
a = input()
if n % 2 == 0:
    print('Ok')
    exit()
for i in a:
    if a.count(i) % 2:
        print(i)
        break