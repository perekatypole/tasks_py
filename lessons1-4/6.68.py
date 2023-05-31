def cancel_fraction(a, b):
    gcd_ab = gcd(a, b)
    return a // gcd_ab, b // gcd_ab

assert cancel_fraction(4, 6) == (2, 3)