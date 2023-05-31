dl = [int(input(f"Введите целое число d{i+1}: ")) for i in range(10)]

summ = 0
for d in dl:
    if d % 2 == 0:
        summ += d

print("Сумма четных целых чисел:", summ)
```

c) Код на Python для вычисления суммы целых чисел, оканчивающихся на 0:

```
l = [int(input(f"Введите целое число {i+1}: ")) for i in range(10)]

summ = 0
for num in l:
    if num % 10 == 0:
        summ += num

print("Сумма целых чисел, оканчивающихся на 0:", summ)