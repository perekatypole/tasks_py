def get_divisors(n):
    return [x for x in range(1, n+1) if n % x == 0]

# Получить сумму всех делителей числа n
def sum_of_divisors(n):
    return sum(get_divisors(n))

# Получить сумму всех четных делителей числа n
def sum_of_even_divisors(n):
    return sum(d for d in get_divisors(n) if d % 2 == 0)

# Определить количество делителей числа n
def count_divisors(n):
    return len(get_divisors(n))

# Определить количество нечетных делителей числа n
def count_odd_divisors(n):
    return sum(1 for d in get_divisors(n) if d % 2 != 0)

# Определить количество четных и нечетных делителей числа n
def count_odd_and_even_divisors(n):
    odd = 0
    even = 0
    for d in get_divisors(n):
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

# Определить количество делителей числа n, больших числа d
def count_divisors_greater_than(n, d):
    return sum(1 for x in get_divisors(n) if x > d)