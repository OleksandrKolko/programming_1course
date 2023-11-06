# https://www.eolymp.com/uk/submissions/15028313
# На привеликий жаль більше 20% не зміг набрати(. Хоча прога працює
def convert_to_10(m, num):
    i = 0
    convert_num = 0
    while num > 0:
        convert_num += (num % 10) * (m ** i)
        num //= 10
        i += 1
    return convert_num


def convert_from_10(k, num):
    converted_num = 0
    result = ''
    i = 0
    if k == 16 or k == 36 and m != 10:
        num = convert_to_10(m, num)
        while num / k != 0:
            if num % k in range(0, 10):
                result += str(num % k)
                num //= k
            elif num % k in range(10, 35):
                result += chr((num % k) + 55)
                num //= k
        return result[::-1]
    if k == 16 or k == 36 and m == 10:
        while num / k != 0:
            if num % k in range(0, 10):
                result += str(num % k)
                num //= k
            elif num % k in range(10, 35):
                result += chr((num % k) + 55)
                num //= k
        return result[::-1]
    else:
        while num / k != 0:
            converted_num += (num % k) * (10 ** i)
            num //= k
            i += 1
        return converted_num


def convert(m, k, num):
    if m > 36 or m < 2 or k > 36 or k < 2:
        return
    if m != 10 and k == 10:
        return convert_to_10(m, num)
    elif m == 10 and k != 10:
        return convert_from_10(k, num)
    elif m != 10 and k != 10:
        return convert_from_10(k, convert_to_10(m, num))


m, k = (int(i) for i in input().split())
num = int(input())
print(convert(m, k, num))