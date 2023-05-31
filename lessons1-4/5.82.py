def find_seven_numbers():
    results = []
    for i in range(100, 1000):
        if i % 7 == 0 and sum([int(digit) for digit in str(i)]) % 7 == 0:
            results.append(i)
    return results