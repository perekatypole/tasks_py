b = [16, 7, 84, 12, 666, 98, 3, 45, 100]
if any(num == 666 for num in b):
    print("Число 666 есть")
    print(f"Порядковый номер первого числа 666: {b.index(next(num for num in b if num == 666)) + 1}")
else:
    print("Числа 666 нет")