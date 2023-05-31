n = int(input("Введите число: "))
flag = True
prev = n % 10
n //= 10
while n > 0:
    current = n % 10
    if current <= prev:
        flag = False
        break
    prev = current
    n //= 10
if flag:
    print("Положительный ответ")
else:
    print("Отрицательный ответ")