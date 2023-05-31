a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Находим наименьшее и второе наименьшее числа
if a <= b and a <= c:
    smallest = a
    if b <= c:
        second_smallest = b
    else:
        second_smallest = c
elif b <= a and b <= c:
    smallest = b
    if a <= c:
        second_smallest = a
    else:
        second_smallest = c
else:
    smallest = c
    if a <= b:
        second_smallest = a
    else:
        second_smallest = b