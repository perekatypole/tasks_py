def integer_division(a, b):
    if b == 0:
        return None
    count = 0
    while a >= b:
        a -= b
        count += 1
    return count

# Остаток от деления без использования оператора %
def remainder(a, b):
    if b == 0:
        return None
    while a >= b:
        a -= b
    return a