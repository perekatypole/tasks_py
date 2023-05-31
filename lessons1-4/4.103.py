x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

max_num = x if x > y else y
min_num = x if x < y else y

print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)

# Использование двух неполных условных операторов:
max_num = x if x > y else y if y > x else x
min_num = x if x < y else y if y < x else x

# Использование одного неполного условного оператора:
max_num, min_num = (x, y) if x > y else (y, x)
print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)