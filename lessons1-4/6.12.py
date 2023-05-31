numbers = []
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    numbers.append(num)
for num in numbers:
    print("Вы ввели число:", num)