def integrate_function():
    def y(x):
        return 0.4 * (x + 2) ** 2 + 1

    a, b = -4, 2
    n = 10000
    dx = (b - a) / n
    sum1 = sum2 = 0

    for i in range(1, n):
        x = a + i * dx
        if y(x) < 2:
            sum1 += y(x)
        else:
            sum2 += y(x)
    return dx * (sum1 + sum2) * 0.5

result = integrate_function()
print(result)