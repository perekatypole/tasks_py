n = 10
fib = [1, 1]
for i in range(2, n):
    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)
print(fib[2:10])