def count_numbers_with_sum(s):
    count = 0
    for i in range(100, 1000):
        if sum(int(digit) for digit in str(i)) == s:
            count += 1
    return count