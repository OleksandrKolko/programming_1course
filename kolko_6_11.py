# https://www.eolymp.com/uk/submissions/14841351
string = input()
criterion_1 = 0
criterion_2 = 0
criterion_3 = 0
criterion_4 = 0
criterion_5 = 0
for i in string:
    if i.islower():
        criterion_1 = 1
    elif i.isupper():
        criterion_2 = 1
    elif i.isdigit():
        criterion_3 = 1
    elif not i.islower() and not i.isupper() and not i.isdigit():
        criterion_4 = 1
if len(string) >= 8:
    criterion_5 = 1
print(criterion_1 + criterion_2 + criterion_3 + criterion_4 + criterion_5)