# https://www.eolymp.com/uk/submissions/15203311
i = int(input())
mas = map(int, input().split())
lis = {}
for el in mas:
    if el not in lis:
        lis[el] = []

print(len(lis))