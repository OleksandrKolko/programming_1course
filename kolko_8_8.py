# https://www.eolymp.com/uk/submissions/15103865
def elevation(num):
    result = ''
    for i in str(bin(num))[3:]:
        if i == '0':
            result += 'S'
        elif i == '1':
            result += 'SX'
    return result


num = int(input())
print(elevation(num))