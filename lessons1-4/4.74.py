a1 = int(input("Введите первую цифру первого числа: "))
a2 = int(input("Введите вторую цифру первого числа: "))
b1 = int(input("Введите первую цифру второго числа: "))
b2 = int(input("Введите вторую цифру второго числа: "))

razn = abs((a2*10 + a1) - (b2*10 + b1))

print("Первая цифра разности: ", razn // 10)
print("Вторая цифра разности: ", razn % 10)