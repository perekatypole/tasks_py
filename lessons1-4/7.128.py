c = [17, 232, 93, 115, 789, 328, 76, 61, 747, 3]
if any(num % 10 == 7 for num in c):
    print("Число, оканчивающееся на 7, есть")
    print(f'Порядковый номер первого числа, оканчивающегося на 7: {c.index(next(num for num in c if num % 10 == 7)) + 1}')
else:
    print("Чисел, оканчивающихся на 7, нет")