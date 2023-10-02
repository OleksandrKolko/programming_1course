# https://www.eolymp.com/uk/submissions/14471244
x = int(input())
couples = 0
sum = 0
while x > 0:
    if (x % 10) % 2 == 0:
        sum += x % 10
        couples += 1
    x //= 10
if couples != 0:
    print(sum)
elif couples == 0:
    print(-1)