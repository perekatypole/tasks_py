distance = 10  # пробег лыжника в первый день
total_distance = distance  # суммарный пробег за первый день
for day in range(2, 11):
    distance *= 1.1  # увеличиваем пробег каждый следующий день на 10%
    total_distance += distance
    if day <= 7:
        print(f'Пробег за {day} день: {distance:.2f}')
print(f'Суммарный пробег за первые 7 дней: {total_distance:.2f}')