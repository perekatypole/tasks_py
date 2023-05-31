def find_squared_number(p):
    n = 1
    while True:
        if n**2 > p:
            return n
        n += 1