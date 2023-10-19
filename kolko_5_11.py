# https://www.eolymp.com/uk/submissions/14801743
n = int(input())
mas = [int(el) for el in input().split()]
res_mas = []
for i in range(len(mas)):
    res_mas.append(mas[-1 + i])
print(*res_mas)