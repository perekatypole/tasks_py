def power_sum(n):
    result = 0
    for i in range(1, n+1):
        result += 2 ** i
    return result