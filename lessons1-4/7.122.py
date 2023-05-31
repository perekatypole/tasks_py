t = int(input("Введите количество чисел: "))
numbers = []
for i in range(t):
    x = int(input("Введите число: "))
    if str(x)[-2:] == "12":
        numbers.append(i + 1)
if len(numbers) > 0:
    print("Номер последнего числа, оканчивающегося цифрами 12: ", numbers[-1])
else:
    print("Среди заданных чисел нет чисел, оканчивающихся цифрами 12.")