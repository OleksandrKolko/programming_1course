# https://www.eolymp.com/uk/submissions/14309005
x, y, x1, y1, x2, y2 = [int(d) for d in input().split()]
x3 = x1
y3 = y2
x4 = x2
y4 = y1
if min(x1, x2, x3, x4) <= x <= max(x1, x2, x3, x4) \
    and min(y1, y2, y3, y4) <= y <= max(y1, y2, y3, y4):
    print("1")
else:
    print("0")