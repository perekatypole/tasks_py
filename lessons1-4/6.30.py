a = 7
b = 23

# Результат целочисленного деления b на a
result = 0
while b >= a:
    b -= a
    result += 1
print("Результат целочисленного деления b на a:", result)

# Остаток от деления b на a
remainder = b
while remainder >= a:
    remainder -= a
print("Остаток от деления b на a:", remainder)