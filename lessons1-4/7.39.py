n = int(input("Введите количество чисел: "))  # п
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

sum_abs = sum([abs(number) for number in numbers])
print("Сумма модулей чисел: ", sum_abs)

prod_abs = 1
for number in numbers:
    prod_abs *= abs(number)
print("Произведение модулей чисел: ", prod_abs)

sum_pairs = [sum(numbers[i:i + 2]) for i in range(n - 1)]
print("Сумма пар чисел:", sum_pairs)

sum_alternate = 0
for i in range(n):
    sign = (-1) ** i
    sum_alternate += sign * numbers[i]
print("Сумма чередующихся знаков чисел:", sum_alternate)