# https://www.eolymp.com/uk/submissions/14292670
side_1, side_2, side_3 = [int(d) for d in input().split()]
if side_1 == side_2 == side_3:
    print(1)
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print(2)
else:
    print(3)