n = int(input("Введите натуральное число: "))
digits = [int(d) for d in str(n)]
max_digit = max(digits)
min_digit = min(digits)
if digits.index(max_digit) < digits.index(min_digit):
    print("Максимальная цифра стоит левее минимальной")
else:
    print("Минимальная цифра стоит левее максимальной")