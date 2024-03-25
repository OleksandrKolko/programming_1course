# https://www.eolymp.com/uk/submissions/14531823
n = int(input())
res = 0
for i in range(10, 100):
    sum = 0
    k = i * n
    while k > 0:
        sum += k % 10
        k //= 10
    if i % 10 + i // 10 == sum :
        res += 1
print(res)