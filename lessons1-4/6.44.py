n = int(input("Введите натуральное число: "))
digits = [int(d) for d in str(n)]
max_digit = max(digits)
min_digit = min(digits)
if (max_digit - min_digit) % 2 == 0:
    print("Разность максимальной и минимальной цифр четная")
else:
    print("Разность максимальной и минимальной цифр нечетная")