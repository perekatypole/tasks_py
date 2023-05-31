def lcm(a, b):
    return a * b // gcd(a, b)

assert lcm(4, 6) == 12