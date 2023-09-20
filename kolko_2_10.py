# https://www.eolymp.com/uk/submissions/14292392
x = int(input())
firs_dig = x // 100
last_dig = x % 10
if firs_dig == last_dig:
    print("=")
else:
    print(max(firs_dig, last_dig))