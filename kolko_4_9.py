# https://www.eolymp.com/uk/submissions/14530580
num_of_dig = int(input())
i = 0
res = ''
while i < num_of_dig:
    x = int(input())
    if x % 2 == 0:
        res += f'{x} is even\n'
        i += 1
    elif x % 2 != 0:
        res += f'{x} is odd\n'
        i += 1
print(res)