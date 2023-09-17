#https://www.eolymp.com/uk/submissions/14200645
x1, y1, x2, y2, a = [str(d) for d in input().split(" ")]
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
a = float(a)
print(f"{format((x1 + (a * x2)) / (1 + a), '.2f')} {format((y1 + (a * y2)) / (1 + a), '.2f')}")