def factorial_sum(n):
    result = 0
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        result += factorial
    return result