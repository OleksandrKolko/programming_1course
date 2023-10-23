# https://www.eolymp.com/uk/submissions/14843743
s = input()
word = ''
print(s[2] + s[6] + s[10])
print(s[0] + s[-2] + s[-1])
print(s[0:7])
print(s[4:])
for i in range(len(s)):
    if i % 2 != 0:
        word += s[i]
print(word)
print(len(word))
print(s[::-1])