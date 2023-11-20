# https://www.eolymp.com/uk/submissions/15157390
num_test = int(input())
for i in range(num_test):
    lis = {}
    lis_max = []
    a = int(input())
    for j in range(a):
        n = int(input())
        if n not in lis:
            lis[n] = [1]
        else:
            lis[n][0] += 1
    for key in lis:
        if lis[key] == max(lis.values()) and key not in lis_max:
            lis_max.append(key)
    if  len(lis_max) == 1:
        print(max(lis_max))
    elif len(lis_max) >= 2:
        print(min(lis_max))