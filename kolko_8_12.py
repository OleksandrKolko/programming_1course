# https://www.eolymp.com/uk/submissions/15168502
def pow_mod(x, y, n):
    if y == 0:
        return 1
    if y % 2 == 1:
        return (x * pow_mod(x * x % n, y // 2, n)) % n
    return pow_mod(x * x % n, y // 2, n)


case = 1
while True:
    k, n, t = map(int, input().split())
    if k + n + t == 0:
        break
    m = 10 ** t
    res = pow_mod(k % m, n, m)
    print(f"Case #{case}: {res}")
    case += 1