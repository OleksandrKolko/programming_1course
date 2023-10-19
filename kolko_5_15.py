# https://www.eolymp.com/uk/submissions/14772318
n = int(input())
lst = [int(el) for el in input().split()]
lst_1 = []
lst_max = max(lst)
lst_min = min(lst)
for el in lst:
    if el == max(lst):
        lst_1.append(lst_min)
    elif el == min(lst):
        lst_1.append(lst_max)
    else:
        lst_1.append(el)
print(*lst_1)