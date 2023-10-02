# https://www.eolymp.com/uk/submissions/14501886
import math
x = int(input())
for i in range(1, 2001):
    if x == math.factorial(i):
        print(i)
        break