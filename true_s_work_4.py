import mymodule
# Програма ламається коли відбувається ділення на ноль. Я знаю що можна було б застосувати функцію переставлення рядків,
# але це буде складновато, для тесту візьміть матрицю 2 1 -1
                                                    # -3 -1 2
                                                    # -2 1 2
# Перевірка функціоналу модуля
print("Перевірка функціоналу модуля")
vec = [1, 0, 0]
mat_1 = mymodule.create_matrix()
mat_2 = mymodule.create_matrix()
mymodule.output_mat(mat_1)
print()
mymodule.output_mat(mat_2)
print()

print("Функція множення матриць")
new_mat = mymodule.mat_scalar(mat_1, mat_2)
mymodule.output_mat(new_mat)
print()

vec_1 = mymodule.mat_vec_scalar(mat_1, vec)
print(vec_1, " Функція множення матриці на вектор")

vec_2 = mymodule.vec_mat_scalar(vec, mat_1)
print(vec_2, " Функція множення вектора на матрицю")
print()

new_mat = mymodule.row_replace(new_mat, 1, 2)
print("Функція переставлення рядків(у прикладі переставляється 1 і 2 рядок)")
mymodule.output_mat(new_mat)
print()

new_mat = mymodule.colum_replase(new_mat, 1, 2)
print("Функція переставлення стовпчиків(у прикладі переставляється 1 і 2 стовпчик)")
mymodule.output_mat(new_mat)
print()
print("Функції множення числа на вектор та віднімання вектора від рядка матриці я застосував у завданні а")

print("Завдання:")
mat = mymodule.create_matrix()
mymodule.output_mat(mat)
print()

#  Завдання а) Перетворення матриці у верхню трикутну
for i in range(len(mat) - 1):

    vec = mymodule.vec_multy(mat[i], 1/(mat[i][i]))  # Створюється вектор, який потім буде
                                                     # відніматись від рядків матриці
    for j in range(i + 1, len(mat)):
        vec = mymodule.vec_multy(vec, mat[j][i])  # Множимо цей вектор на нижній елемент,
                                                  # щоб при відніманнфі утворився 0
        mat[j] = mymodule.vec_sub(mat, vec, j)
        mymodule.output_mat(mat)  # Вивожу матрицю, щоб можна було бачити резултати дій програми
        print()
        vec = mymodule.vec_multy(mat[i], 1 / (mat[i][i]))  # Повертаємо цьому вектору значення і-того стовпчика
                                                           # та продовжуємо алгоритм

# Завдвання б) Визначення рангу матриці
rank_of_mat = len(mat)
zero_row = True
for row in mat:
    for el in row:
        if el != 0:
            zero_row = False
            break
        zero_row = True
    if zero_row:  # Якщо матриця буде мати нульовий рядок, то ранг матриці зменьшується
        rank_of_mat -= 1
print(f"Ранг матриці - {rank_of_mat}")

# Завдання в) Обчислення визначника
# Через те, що ми звели вид матриці до верхньої трикутної, то визначник дорівнює добутку елементів головної діагоналі
det = 1
for i in range(len(mat)):
    det *= mat[i][i]
print(f"Визначник дорівнює - {det}")