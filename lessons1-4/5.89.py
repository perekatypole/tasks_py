def count_seven_numbers():
    count = 0
    for i in range(100, 1000):
        if i % 7 == 0 and sum(int(digit) for digit in str(i)) % 7 == 0:
            count += 1
    return count