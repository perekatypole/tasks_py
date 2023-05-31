def count_numbers_with_sum_of_digits():
    count = 0
    for i in range(100, 501):
        if sum(int(digit) for digit in str(i)) == 15:
            count += 1
    return count