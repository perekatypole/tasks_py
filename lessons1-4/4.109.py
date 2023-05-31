a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= 0:
    a_squared = a ** 2
else:
    a_squared = a

if b >= 0:
    b_squared = b ** 2
else:
    b_squared = b

if c >= 0:
    c_squared = c ** 2
else:
    c_squared = c

print("Квадрат первого числа:", a_squared)
print("Квадрат второго числа:", b_squared)
print("Квадрат третьего числа:", c_squared)