# https://www.eolymp.com/uk/submissions/14801695
n = int(input())
mas_1 = [int(el) for el in input().split()]
m = int(input())
mas_2 = [int(el) for el in input().split()]
res_mas = []
for el_1 in mas_1:
    if el_1 not in mas_2:
        res_mas.append(el_1)
print(len(res_mas))
print(*res_mas)