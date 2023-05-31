# определяем, выполняется ли условие
def check_number(n, a, b):
    digit_sum = 0
    digit_product = 1
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_product *= digit
        n //= 10
    if digit_sum < a and digit_product > b:
        return True
    else:
        return False