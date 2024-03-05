a = int(input("Введіть коефіціент біля x^2 - "))
b = int(input("Введіть коефіціент біля x - "))
c = int(input("Введіть вільний член - "))
assert a != 0, "Коефіціент а не може бути рівним нулю, тоді це рівняння не буде квадратним"
print((b ** 2) - 4 * a * c)
x = 0
assert ((b ** 2) - 4 * a * c) >= 0, "Це рівняння не має розв'язків над полем дійсних чисел"
dis = (b ** 2) - 4 * a * c
if dis == 0:
    x = (b * -1) / (2 * a)
    print(f"Це рівняння має один корінь - {format(x, '.0f')}")
elif dis > 0:
    x_1 = ((b * -1) - dis ** 0.5) / (2 * a)
    x_2 = ((b * -1) + dis ** 0.5) / (2 * a)
    print(f"Це рівняння має два кореня - {format(x_1, '.0f')} {format(x_2, '.0f')}")