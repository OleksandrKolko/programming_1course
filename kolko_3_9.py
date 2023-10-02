# https://www.eolymp.com/uk/submissions/14402752
n = int(input())
correct_numbers = 0
number = 0
while correct_numbers < n:
    if number % 2 != 0 and number % 5 != 0 and number % 3 != 0:
        correct_numbers += 1
        print(number, end=' ')
        number += 1
    else:
        number += 1