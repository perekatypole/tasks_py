a = [int(input(f"Введите целое число a{i+1}: ")) for i in range(20)]

summ = 0
for i in range(1, len(a), 2):
    summ += a[i]