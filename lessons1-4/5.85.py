def find_kaprekar_numbers():
    results = []
    for i in range(10, 100):
        square = i ** 2
        string_square = str(square).zfill(4)
        left, right = string_square[:2], string_square[2:]
        if i == int(left) + int(right):
            results.append(i)
    return results