# https://www.eolymp.com/uk/submissions/15000028
def nsd(a, b):
    if b == 0:
        return a
    else:
        return nsd(b, a % b)


def nsk(a, b):
    return a * b // nsd(a, b)


a, b = input().split()
a = int(a)
b = int(b)
count = 0
for i in range(1, b + 1):
    if (a * b) % i == 0:
        if nsd((a * b) / i, i) == a and nsk((a * b) / i, i) == b:
            count += 1

    else:
        continue
print(count)