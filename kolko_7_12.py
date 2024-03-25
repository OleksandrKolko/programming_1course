# https://www.eolymp.com/uk/submissions/15028649
# Тупо не вистачає часу
def count_ones_in_binary_range(a, b):
    count = 0
    for num in range(a, b + 1):
        binary_representation = bin(num)
        count += binary_representation.count('1')
    return count


a, b = map(int, input().split())
result = count_ones_in_binary_range(a, b)
print(result)