def is_perfect(n):
    if n <= 1:
        return False
    return sum(x for x in range(1, n) if n % x == 0) == n
