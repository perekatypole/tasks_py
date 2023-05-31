def is_same_digits(num):
    digits = str(num)
    return all(d == digits[0] for d in digits)

def has_adjacent_digits(num):
    digits = str(num)
    for i in range(1, len(digits)):
        if digits[i] == digits[i - 1]:
            return True
    return False

num_1 = 666
num_2 = 35510

print(is_same_digits(num_1)) # True
print(is_same_digits(num_2)) # False
print(has_adjacent_digits(num_1)) # False
print(has_adjacent_digits(num_2)) # True