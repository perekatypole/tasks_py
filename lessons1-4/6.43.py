number = int(input("Введите натуральное число: "))
digits = [int(digit) for digit in str(number)]
max_digit = max(digits)
min_digit = min(digits)
a = int(input("Введите a: "))
sum_digits = max_digit + min_digit
if sum_digits % a == 0:
    print("Сумма максимальной и минимальной цифр кратна a!")
else:
    print("Сумма максимальной и минимальной цифр не кратна a")