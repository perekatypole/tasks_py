t = 12345
m = 3
sum = 0
while t > 0 and m > 0:
    last_digit = t % 10
    sum += last_digit
    t //= 10
    m -= 1
print("Сумма последних цифр:", sum)