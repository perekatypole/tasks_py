x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

if x > 0:
    if y > 0:
        print("Точка находится в области I")
    else:
        print("Точка находится в области IV")
else:
    if y > 0:
        print("Точка находится в области II")
    else:
        print("Точка находится в области III")


