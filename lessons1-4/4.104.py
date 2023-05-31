x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

half_sum = (abs(x) + abs(y)) / 2
sqrt_prod = math.sqrt(abs(x) * abs(y))

print("Полусумма абсолютных величин:", half_sum)
print("Квадратный корень из произведения абсолютных величин:", sqrt_prod)