def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    half_power = power(a, n // 2)
    return half_power * half_power * power(a, n % 2)