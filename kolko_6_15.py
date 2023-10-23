# https://www.eolymp.com/uk/submissions/14843470
# Дивна задачка. Програма наче працює коректно, але видає лише 70%.
string = input()
pun = '!"#$%&()*+,./:;<=>?@[]^`-_{|}~'
for i in string:
    for j in pun:
        if i == j:
            string = string.replace(i, '')
string = string.lower().split()
mas = [len((_)) for _ in string]
res = 0
for i in string:
    if len(i) > 1 and i == i[::-1] and len(i) == max(mas):
        print(string.index(i) + 1)
        res = 1
        break
if res == 0:
    print(0)