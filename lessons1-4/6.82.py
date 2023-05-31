n = int(input())
is_non_decreasing = True
prev_digit = n % 10
n //= 10

while n > 0 and is_non_decreasing:
    curr_digit = n % 10
    is_non_decreasing = curr_digit <= prev_digit
    prev_digit = curr_digit
    n //= 10

if is_non_decreasing:
    print("Положительный")
else:
    print("Отрицательный")