def find_square_numbers():
    results = []
    for i in range(100, 1000):
        square = i ** 2
        if square % 1000 == i:
            results.append(i)
    return results