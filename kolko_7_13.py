# https://www.eolymp.com/uk/submissions/15029220
def is_correct_num(num):
    for i in str(num):
        if str(num).count(i) > 1:
            return False
    return True


def result(a, b):
    for el in range(a, b + 1):
        if is_correct_num(el):
            print(el, end=" ")
        else:
            continue


a, b = map(int, input().split())
result(a, b)