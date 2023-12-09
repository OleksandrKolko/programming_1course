def create_matrix():  # Створення квадратної матриці
    mat = []
    n = int(input("Введіть розмірність матриці: "))
    for i in range(1, n + 1):
        row = [int(el) for el in input(f"Рядкок {i}: ").split()]
        if len(row) > n or len(row) < n:
            raise "Кількість елементів не відповідає розмірності матриці!"
        mat.append(row)
    return mat


def mat_vec_scalar(mat, vec):  # Множення матриці на вектор
    new_vec = []
    for i in range(len(mat)):
        res = 0
        for j in range(len(mat)):
            res += mat[i][j] * vec[j]
        new_vec.append(res)
    return new_vec


def vec_mat_scalar(vec, mat):  # Множення вектора на матрицю
    new_vec = []
    for i in range(len(mat)):
        res = 0
        for j in range(len(mat)):
            res += vec[j] * mat[j][i]
        new_vec.append(res)
    return new_vec


def output_mat(mat):  # Виведення матриці. На жаль, у мене не вийшло реалізувати схоже виведення, але з числами без ".0"
    for row in mat:
        print('', *row, sep='| ', end= '| \n')


def row_replace(mat,row_1, row_2):  # Перестановка рядків
    row_1 -= 1
    row_2 -= 1
    mat[row_1], mat[row_2] = mat[row_2], mat[row_1]
    return mat


def get_row(mat, row_num):  # Отримання певного рядка
    row_num -= 1
    return mat[row_num]


def colum_replase(mat, colum_1, colum_2):  # Перестановка стовпчиків
    colum_1 -= 1
    colum_2 -= 1
    for i in range(len(mat)):
        mat[i][colum_1], mat[i][colum_2] = mat[i][colum_2], mat[i][colum_1]
    return mat


def mat_scalar(A, B):  # Множення матриці
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


def vec_multy(vec, num):  # Множення числа на вектор
    new_vec = []
    for i in range(len(vec)):
        vec[i] *= num
    new_vec = vec.copy()
    return new_vec


def vec_sub(mat, vec, row_num):  # Віднамання вектора від рядка матриці
    for i in range(len(mat[row_num])):
        mat[row_num][i] = mat[row_num][i] - vec[i]
    return mat[row_num]
