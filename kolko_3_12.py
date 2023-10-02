# https://www.eolymp.com/uk/submissions/14501674
n = int(input()) 
a = 0 
while str(n) != str(n)[::-1]: 
    a += 1 
    n += int(str(n)[::-1]) 
print(a)