# https://www.eolymp.com/uk/submissions/14842431
string = input()
k = int(input())
field = [int(_) for _ in range(ord('A'), ord('Z') + 1)]
for i in string:
    print(chr(field[ord(i) - k - 65]), end='')