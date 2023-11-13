# Тут без силки на е-олімп бо там по 0. Ну головне що чісла Фібоначі знаходить і НСД.
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


def nsd(a, b):
    if b == 0:
        return a % 10 ** 8
    else:
        return nsd(b, a % b)


A = [[1, 1],
     [1, 2]]
B = [[1],
     [1]]


def fibonachi(n):
    A1 = A
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n % 2 == 0:
        for i in range(int(n / 2) - 1):
            result = mat_scalar(A1, A)
            A1 = result
        return mat_scalar(A1, B)[0]
    elif n % 2 != 0:
        for i in range(int((n - 1) / 2) - 1):
            result = mat_scalar(A1, A)
            A1 = result
        return mat_scalar(A1, B)[1]


while True:
    n, m = map(int, input().split())
    print(nsd(*fibonachi(n), *fibonachi(m)))