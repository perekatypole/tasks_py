def max_odd_digit(n):
    max_odd = -1
    while n > 0:
        digit = n % 10
        if digit % 2 == 1 and digit > max_odd:
            max_odd = digit
        n //= 10
    return max_odd


# определяем номер минимальной цифры
def min_digit_index(n):
    min_digit = n % 10
    index = 0
    pos = 0
    while n > 0:
        digit = n % 10
        pos += 1
        if digit <= min_digit:
            min_digit = digit
            index = pos
        n //= 10
    return index