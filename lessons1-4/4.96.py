a = int(input("Введите номер первой квартиры: "))
p = int(input("Введите количество квартир: "))

sum = 0
for i in range(a, a+p):
    sum += i

if sum % 2 == 0:
    print("Сумма номеров всех квартир - четное число")
else:
    print("Сумма номеров всех квартир - нечетное число")