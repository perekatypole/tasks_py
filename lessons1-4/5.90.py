def check_fibonacci_sum(p):
    a, b = 0, 1
    summa = 0
    for i in range(p):
        summa += a
        a, b = b, a+b
    return summa == (b-1)