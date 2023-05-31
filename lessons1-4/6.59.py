num = int(input("Введите число: "))
min_digit = 9
count = 0

for digit in str(num):
    if int(digit) < min_digit:
        min_digit = int(digit)

for digit in str(num):
    if int(digit) == min_digit:
        count += 1

print("Минимальная цифра в числе: ", min_digit)
print("Количество вхождений минимальной цифры: ", count)