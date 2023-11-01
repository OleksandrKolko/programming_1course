#https://www.eolymp.com/uk/submissions/14200755
import math
x, y = [str(d) for d in input().split(" ")]
x = float(x)
y = float(y)
first_part = ((2 * x * y) / math.sqrt((x**2) + (y**2)))
second_part = (((x + y - 1)**2) / (x * y))
result = first_part - second_part
print(format(result, '.3f'))