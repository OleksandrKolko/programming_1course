# https://www.eolymp.com/uk/submissions/15018570
def is_lucky(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    for j in range(2, int(int(str(num)[::-1]) ** 0.5) + 1):
        if int(str(num)[::-1]) % j == 0:
            return False
    if str(num) == str(num)[::-1]:
        return False
    return True


def index_of_lucky_num(k):
    i = 0
    last_num = 10
    while i != k:
        for num in range(last_num + 1, 100 * k):
            if is_lucky(num):
                last_num = num
                break
        i += 1
    if num > 10 ** 6:
        return 1
    return num


k = int(input())
print(index_of_lucky_num(k))