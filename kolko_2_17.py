# https://www.eolymp.com/uk/submissions/14302215
# вибачте, забув як переносити частину умов)
x_c, y_c = [int(d) for d in input().split()]
x_a, y_a = [int(d) for d in input().split()]
x_b, y_b = [int(d) for d in input().split()]
x_ca = x_a - x_c
y_ca = y_a - y_c
x_ab = x_b - x_a
y_ab = y_b - y_a
if x_ca * y_ab == x_ab * y_ca:
    print("YES")
else:
    print("NO")
if (x_a <= x_b and x_a <= x_c and y_a <= y_b and y_a <= y_c and x_ca * y_ab == x_ab * y_ca) or (x_a >= x_b and x_a >= x_c and y_a >= y_b and y_a >= y_c and x_ca * y_ab == x_ab * y_ca):
    print("YES")
else:
    print("NO")
if ((x_a <= x_c <= x_b or x_b <= x_c <= x_a) and (y_a <= y_c <= y_b or y_b <= y_c <= y_a)) and x_ca * y_ab == x_ab * y_ca:
    print("YES")
else:
    print("NO")