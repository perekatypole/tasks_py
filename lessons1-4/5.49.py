deposit = 1000  # начальная сумма вклада
interest_rate = 0.02  # годовая процентная ставка
for i in range(1, 13):
    increment = deposit * interest_rate / 12  # прирост суммы вклада за месяц
    deposit += increment
    if i <= 10:
        print(f'Прирост за {i} месяц: {increment:.2f}, сумма вклада: {deposit:.2f}')
    if i in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        print(f'Сумма вклада через {i} месяцев: {deposit:.2f}')