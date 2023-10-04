n = int(input())
res = 1
for i in range(1, n + 1):
    if i % 8 == 0:
        res *= i       
print(res)