# определяем, выполнено ли условие
def check_number(n):
    if n < 1000 or n > 9999 or n % 2 == 1:
        return False
    # проверяем сумму и произведение цифр
    digit_sum = 0
    digit_product = 1
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_product *= digit
        if digit > 6:
            return False
        n //= 10
    if digit_sum <= 10 or digit_product >= 50:
        return False
    # проверяем количество цифр и первую/последнюю цифры
    num_digits = len(str(n))
    if num_digits % 2 != 0 or str(n)[0] != str(n)[-1]:
        return False
    # определяем, какая цифра больше
    if int(str(n)[0]) > int(str(n)[-1]):
        return 'First digit is greater'
    elif int(str(n)[0]) < int(str(n)[-1]):
        return 'Last digit is greater'
    else:
        return 'First and last digit are equal'