def cube(n):
    result = 1
    for i in range(n):
        result += 2 * i * (i + 1)
    return result