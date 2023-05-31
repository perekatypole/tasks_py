num = int(input("Введите число: "))
max_digit = 0
count = 0

for digit in str(num):
    if int(digit) > max_digit:
        max_digit = int(digit)

for digit in str(num):
    if int(digit) == max_digit:
        count += 1

print("Максимальная цифра в числе: ", max_digit)
print("Количество вхождений максимальной цифры: ", count)