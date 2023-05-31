# Ввод 10 чисел с проверкой на 0
numbers = []
for i in range(10):
    num = int(input("Введите число: "))
    if num == 0:
        break
    numbers.append(num)