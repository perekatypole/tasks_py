x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
if x > 0 and y > 0 and x**2 + y**2 < 1:
    print("Точка попадает в область I")
else:
    print("Точка не попадает в область I")