# https://www.eolymp.com/uk/submissions/14293178
a, b, c = [int(d) for d in input().split()]
dis = (b**2) - (4 * a * c)
if dis > 0:
    x1 = (-b - dis**0.5) / (2 * a)
    x2 = (-b + dis**0.5) / (2 * a)
    print(f'Two roots: {round(min(x1, x2))} {round(max(x1, x2))}')
elif dis == 0:
    x1 = (-b)/(2 * a)
    print(f'One root: {round(x1)}')
else:
    print("No roots")