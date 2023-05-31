def sum_of_largest_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[-1] + numbers[-2]

result = sum_of_largest_numbers(5, 10, 3)
print(result)