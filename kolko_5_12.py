# https://www.eolymp.com/uk/submissions/14801776
n = int(input())
mas = [int(el) for el in input().split()]
res_mas = []
for el in mas:
    if el not in res_mas:
        res_mas.append(el)
print(*res_mas)