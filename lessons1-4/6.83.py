n = int(input())
is_increasing = True
prev_digit = n % 10
n //= 10

while n > 0 and is_increasing:
    curr_digit = n % 10
    is_increasing = curr_digit > prev_digit
    prev_digit = curr_digit
    n //= 10

if is_increasing:
    print("Положительный")
else:
    print("Отрицательный")