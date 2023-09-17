#https://www.eolymp.com/uk/submissions/14200440
import math
s, r1 = [str(d) for d in input().split(" ")]
s = abs(float(s))
r1 = abs(float(r1))
r2 = math.sqrt((r1**2) - (s / math.pi))
print(format(r2, '.2f'))