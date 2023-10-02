# https://www.eolymp.com/uk/submissions/14504287
seq = [1,] + [5 ** (2 ** n) % 10 ** n for n in range(10)] + [16 ** (5 ** n) % 10 ** n for n in range(10)]
seq.sort(reverse=True)
n = int(input())
for x in seq:
    if x <= n:
        print(x)
        break