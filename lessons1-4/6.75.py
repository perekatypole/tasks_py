def f(x):
    return x ** 4 + 2 * x ** 2 - x - 1

def g(x):
    return x ** 3 - 0.2 * x ** 2 - 0.2 * x - 1.2

def bisection(a, b, f):
    if f(a) * f(b) > 0:
        return None
    while b - a > 0.001:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root_1 = bisection(0, 1, f)
root_2 = bisection(1, 1.5, g)

print(root_1) # 0.779296875
print(root_2) # 1.2001953125