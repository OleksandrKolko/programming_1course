# https://www.eolymp.com/uk/submissions/14801347
# Дивна задачка. Помилки не знайшов, але всеодно видає лише 50%.
a, b, c, d = [int(_) for _ in input().split()]
res = 0
mas = []
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if i * j not in mas:
            res += 1
            mas.append(i * j)
print(len(mas))