# https://www.eolymp.com/uk/submissions/14533831
n = int(input())
prime_num = 1
for i in range(2, int(n ** 0.5 + 1)):
    if n % i == 0:
        prime_num = 0
        break
if prime_num == 0:
    i = 2
    while True:
        if n % i == 0:
            break
        i += 1
    print(format(n / i, '.0f'))
else:
    print(1)