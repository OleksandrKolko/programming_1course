# https://www.eolymp.com/uk/submissions/15155975
import math
n = int(input())
row = map(int, input().split())
row = set(row)
lis = {}
for i in row:
    if abs(i) not in lis:
        lis[abs(i)] = []
print(len(lis))