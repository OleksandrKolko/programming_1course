#https://www.eolymp.com/uk/submissions/14200741
x, y = [str(d) for d in input().split(" ")]
x = float(x)
y = float(y)
first_part = (((x**2) - (2 * x * y) + (4 * (y**2))) / (x + 5))
second_part = (((3 * (x**2)) - (y**2)) / ( y - 7))
result = first_part + second_part
print(format(result, '.3f'))