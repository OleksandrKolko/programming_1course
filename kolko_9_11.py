# https://www.eolymp.com/uk/submissions/15204497
# Не зміг знайти помилку, наче все норм)
n, m = map(int, input().split())
lis = []
text = []
marks = ".,:;\'\"!?-`()/\\@#$%^&*"
good_text = True

for _ in range(n):
    word = input().lower()
    lis.append(word)

for _ in range(m):
    line = input()
    for mark in marks:
        line = line.replace(mark, '')
    line = line.lower().split()
    text += line

for word in text:
    if word not in lis:
        print("Some words from the text are unknown.", end=' ')
        good_text = False
        break
for el in lis:
    if el not in text:
        print("The usage of the vocabulary is not perfect.", end=' ')
        good_text = False
        break
if good_text:
    print("Everything is going to be OK.")