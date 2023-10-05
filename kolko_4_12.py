# https://www.eolymp.com/uk/submissions/14530995
res = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n % 2 == 0:
        res += n
print(res)