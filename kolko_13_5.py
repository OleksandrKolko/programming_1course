def ex_a(line):
    result = 0
    for el in line:
        if int(el) % 2 == 0:
            result += 1
    return result


def ex_b(line):
    result = 0
    for el in line:
        if (int(el) ** 0.5) % 2 == 1:
            result += 1
    return result


def ex_c(line):
    return max(line) - min(line)


def ex_d(line):
    mas_len = []
    length = 1
    for i in range(len(line) - 1):
        if i + 1 == len(line) - 1 and line[i] < line[i + 1]:
            length += 1
            mas_len.append(length)
            break
        if line[i] < line[i + 1]:
            length += 1
        elif line[i] > line[i + 1]:
            mas_len.append(length)
            length = 1
    if not mas_len:
        return "Файл не містить зростаючої послідовності"
    return max(mas_len)


with open("") as file:
    mas_of_lines = []
    for line in file:
        line = [int(el) for el in line.split()]
        mas_of_lines += line
    print(f"Результат завдання a): {ex_a(mas_of_lines)}")
    print(f"Результат завдання b): {ex_b(mas_of_lines)}")
    print(f"Результат завдання c): {ex_c(mas_of_lines)}")
    print(f"Результат завдання d): {ex_d(mas_of_lines)}")