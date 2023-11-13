# https://www.eolymp.com/uk/submissions/15104295
alphabet = '0123456789ABC'


def convert_from_10(num):
    converted_num = ''
    while num != 0:
        converted_num += alphabet[num % 13]
        num //= 13
    return converted_num[::-1]


num = int(input())
print(convert_from_10(num))