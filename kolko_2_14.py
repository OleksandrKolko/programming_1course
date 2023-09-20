# https://www.eolymp.com/uk/submissions/14293256
score = int(input())
if 0 < score <= 3:
    print("Initial")
elif 4 <= score <= 6:
    print("Average")
elif 7 <= score <= 9:
    print("Sufficient")
elif 10 <= score <= 12:
    print("High")