number = int(input("Введите натуральное число: "))
digits = [int(digit) for digit in str(number)]
max_digit = max(digits)
min_digit = min(digits)
print("Максимальная цифра -", max_digit)
print("Минимальная цифра -", min_digit)
print("Разница -", max_digit - min_digit)
print("Сумма -", max_digit + min_digit)