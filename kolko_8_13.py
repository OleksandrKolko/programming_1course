# https://www.eolymp.com/uk/submissions/15168987. 61%, далі не проходить по часу, навіть бінарне піднесення використав.
from math import gcd


def mat_scalar(A, B):
    new_mat = []
    for i in range(len(A)):
        row = []
        for k in range(len(B[i])):
            res = 0
            for j in range(len(A[i])):
                res += A[i][j] * B[j][k]
            row.append(res)
        new_mat.append(row)
    return new_mat


def elevation(num):
    result = ''
    for i in str(bin(num))[3:]:
        if i == '0':
            result += 'S'
        elif i == '1':
            result += 'SX'
    return result


A = [[1, 1],
     [1, 2]]
B = [[1],
     [1]]


def fib(n):
    A1 = A
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 == 0:
        for el in elevation(int((n - 1) / 2)):
            if el == 'S':
                res = mat_scalar(A1, A1)
                A1 = res
            elif el == 'X':
                res = mat_scalar(A1, A)
                A1 = res
        return mat_scalar(A1, B)[1][0] % (10 ** 8)
    elif n % 2 != 0:
        for el in elevation(int((n - 1) / 2)):
            if el == 'S':
                res = mat_scalar(A1, A1)
                A1 = res
            elif el == 'X':
                res = mat_scalar(A1, A)
                A1 = res
        return mat_scalar(A1, B)[0][0] % (10 ** 8)


while True:
    try:
        n, m = map(int, input().split())
        print(fib(gcd(n, m)))
    except EOFError:
        break
