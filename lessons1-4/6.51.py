# определяем, выполняется ли условие
def check_number(n, k, b, x, y, a, t, n):
    digit_sum = 0
    num_digits = 0
    digit_product = 1
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_product *= digit
        num_digits += 1
        if num_digits > b:
            return False
        if digit == y:
            break
        n //= 10
    if digit_sum <= k or num_digits % 2 != 0:
        return False
    if digit_product < a or n % b != 0:
        return False
    if x != str(n)[0] or y != str(n)[-1]:
        return False
    if digit_sum <= t:
        return True
    else:
        return False

