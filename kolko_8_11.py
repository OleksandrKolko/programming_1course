# https://www.eolymp.com/uk/submissions/15109508
def funk_1(n):
    while n != 0:
        if n % 10 > 0:
            return n % 10
        elif n == 0:
            return 0
        else:
            n /= 10


def funk_2(p, q):
    res = 0
    for n in range(p, q + 1):
        res += funk_1(n)
    return int(res)


while True:
    p, q = map(int, input().split())
    if p == -1 and q == -1:
        break
    else:
        print(funk_2(p, q))