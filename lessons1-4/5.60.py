def multiply(p, a):
    result = 0
    for i in range(abs(p)):
        result += a * (-1 if p < 0 else 1)
    return result if p >= 0 else -result