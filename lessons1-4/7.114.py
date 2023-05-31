numbers = [dv, d2, d3, d4, dl4]  # список заданных чисел
even_numbers = [n for n in numbers if n % 2 == 0]  # список четных чисел
if even_numbers:
    avg = sum(even_numbers) / len(even_numbers)  # среднее арифметическое
    print(avg)
else:
    print("Нет четных чисел")