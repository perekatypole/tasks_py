d = [12, 49, 21, 7, 90, 22, 35, 28, 77, 0, -1]
if any(num % 7 == 0 for num in d):
    print("Число, кратное 7, есть")
    print(f"Порядковый номер первого числа, кратного 7: {d.index(next(num for num in d if num % 7 == 0)) + 1}")
else:
    print("Чисел, кратных 7, нет")