# https://www.eolymp.com/uk/submissions/15207012
n = int(input())
lis = {}
new_lis = {}

for i in range(n):
    a = input()
    a = a.replace(',', '').replace('-', '').split()
    lis[a[0]] = []
    for j in range(1, len(a)):
        lis[a[0]].append(a[j])

for key, value in lis.items():
    for el in value:
        if el not in new_lis:
            new_lis[el] = []
            new_lis[el].append(key)
        else:
            new_lis[el].append(key)

sorted_lis = sorted(new_lis)
print(len(new_lis))
for key in sorted_lis:
    print(key, '-', end=' ')
    print(*new_lis[key], sep=', ')