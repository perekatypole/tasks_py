def find_numbers(n):
    results = []
    for i in range(10, 100):
        if i % n == 0 or str(n) in str(i):
            results.append(i)
    return results