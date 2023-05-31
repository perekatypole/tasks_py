n = 10
fib = [1, 1]
for i in range(2, n):
    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)
print(fib)

m = 7 # Получить значение 7-го члена
f_7 = fib[m-1]
print(f_7)