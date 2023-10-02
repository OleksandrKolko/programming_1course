# https://www.eolymp.com/uk/submissions/14452086
x = int(input())
i = 1
correct_x = 0
while x > 0:
    if (x % 10) % 2 == 0 or (x % 10) == 0:
        x += 1
    elif (x % 10) % 2 != 0:
        x -= 1
    correct_x += (x % 10) * i
    i *= 10
    x //= 10
print(correct_x)