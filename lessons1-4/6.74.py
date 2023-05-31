def is_power_of_three(num):
    if num <= 0:
        return False
    while num > 1:
        if num % 3 != 0:
            return False
        num = num // 3
    return True

def is_power_of_five(num):
    if num <= 0:
        return False
    while num > 1:
        if num % 5 != 0:
            return False
        num = num // 5
    return True