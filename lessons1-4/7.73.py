t = 5
x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_div_3 = sum(1 for x in x_list if x % 3 == 0)
x_div_7 = sum(1 for x in x_list if x % 7 == 0)

print("Количество чисел, кратных 3:", x_div_3)
print("Количество чисел, кратных 7:", x_div_7)