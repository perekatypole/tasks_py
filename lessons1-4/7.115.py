numbers = [яр, а2, ..., яш]  # список заданных чисел
p = 7  # число, на которое проверяем кратность
p_numbers = [n for n in numbers if n % p == 0]  # список чисел, кратных p
if p_numbers:
    avg = sum(p_numbers) / len(p_numbers)  # среднее арифметическое
    print(avg)
else:
    print("Нет чисел, кратных", p)