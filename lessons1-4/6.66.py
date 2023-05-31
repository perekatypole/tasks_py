def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)

assert gcd_three(12, 18, 24) == 6