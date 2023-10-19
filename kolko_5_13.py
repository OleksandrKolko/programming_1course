# https://www.eolymp.com/uk/submissions/14801907
# В цій задачці можна було обійтись без додаткового масиву і відразу все рахувати, але у мене вже була зроблена основна частина тому мені було ліньки впиравляти)
n = int(input())
mas = [float(el) for el in input().split()]
res_mas = []
sum = 0
for el in mas:
    if el > 0:
        res_mas.append(el)
if len(res_mas) != 0:
    for el in res_mas:
        sum += el
    print(format(sum/len(res_mas), '.2f'))
else:
    print("Not Found")