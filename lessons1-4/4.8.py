import math

x = float(input("Введите значение x: "))
a = float(input("Введите значение угла a в градусах: "))

if math.sin(math.radians(a)) > 0:
    k = x**2
else:
    k = abs(x)

if x < k:
    f = x*k
else:
    f = k*x

print("Значение функции равно", f)