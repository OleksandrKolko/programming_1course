# https://www.eolymp.com/uk/submissions/14999592
def nsd(a, b):
    if b == 0:
        return a
    else:
        return nsd(b, a % b)


def nsk(a, b):
    return a*b//nsd(a, b)


n = int(input())
c = 1
for i in range(1, n+1):
    c = nsk(c, i)
print(c)