def find_number(factorial):
    n = 1
    result = 1
    while result < factorial:
        n += 1
        result *= n
    return n