python
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a > b:
    max_num = a
    min_num = b
else:
    max_num = b
    min_num = a

print("Максимальное значение:", max_num)
print("Минимальное значение:", min_num)