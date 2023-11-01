#https://www.eolymp.com/uk/submissions/14200715
import math
a, b, c, d, f = [str(d) for d in input().split(" ")]
a = float(a)
b = float(b)
c = float(c)
d = float(d)
f = float(f)
if a > 0 and b > 0 and c > 0 and c > 0 and d > 0 and f <= 100:
    p1 = (a + b + f) / 2
    p2 = (c + d + f) / 2
    s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - f))
    s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - f))
    s = s1 + s2
print(format(s, '.4f'))