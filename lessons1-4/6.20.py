number = 12345

# Сумма цифр
sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print("Сумма цифр:", sum)

# Количество цифр
count = 0
while number > 0:
    count += 1
    number //= 10
print("Количество цифр:", count)

# Произведение цифр
product = 1
while number > 0:
    digit = number % 10
    product *= digit
    number //= 10
print("Произведение цифр:", product)

# Среднее арифметическое цифр
sum = 0
count = 0
while number > 0:
    digit = number % 10
    sum += digit
    count += 1
    number //= 10
average = sum / count
print("Среднее арифметическое цифр:", average)

# Сумма квадратов цифр
sum = 0
while number > 0:
    digit = number % 10
    sum += digit**2
    number //= 10
print("Сумма квадратов цифр:", sum)

# Сумма кубов цифр
sum = 0
while number > 0:
    digit = number % 10
    sum += digit**3
    number //= 10
print("Сумма кубов цифр:", sum)

# Первая цифра
while number >= 10:
    number //= 10
print("Первая цифра:", number)

# Сумма первой и последней цифры
last_digit = number % 10
while number >= 10:
    number //= 10
first_digit = number
print("Сумма первой и последней цифры:", first_digit + last_digit)