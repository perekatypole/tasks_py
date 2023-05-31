n = int(input("Введите натуральное число: "))
digits = [int(d) for d in str(n)]
max_digit = max(digits)
min_digit = min(digits)
max_index_from_end = len(digits) - digits.index(max_digit)
min_index_from_end = len(digits) - digits.index(min_digit)
max_index_from_start = digits.index(max_digit) + 1
min_index_from_start = digits.index(min_digit) + 1
print("Порядковый номер максимальной цифры от конца числа:", max_index_from_end)
print("Порядковый номер минимальной цифры от конца числа:", min_index_from_end)
print("Порядковый номер максимальной цифры от начала числа:", max_index_from_start)
print("Порядковый номер минимальной цифры от начала числа:", min_index_from_start)