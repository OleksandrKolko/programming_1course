# https://www.eolymp.com/uk/submissions/14502289
k = int(input())
n = int(input())
i = 0
convert_num = 0
while n > 0:
    convert_num += (n % 10) * (k ** i)
    n //= 10
    i += 1
print(convert_num)