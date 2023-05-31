temperatures = [2, 3, -1, -4, 0, 2, -3, -2, 1, 0, 1, -5]
count_below_zero = 0
for temperature in temperatures:
    if temperature < 0:
        count_below_zero += 1
print("Количество опусканий температуры ниже нуля:", count_below_zero)