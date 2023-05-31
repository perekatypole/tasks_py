rainfall = [0, 0, 0, 0.5, 0.8, 1.2, 0, 1.3, 1.8, 2.3, 0, 1.5, 2.5, 4.3, 0, 0, 1.8, 0, 0, 0, 1.3, 0.8, 0, 0, 0.1, 0, 0, 0.7, 0.9, 1.2]
no_rain_days = 0
for rainfall_today in rainfall:
    if rainfall_today == 0:
        no_rain_days += 1
if no_rain_days >= 10:
    print("Было более 10 дней без осадков")
else:
    print("Все дни марта были дождливыми")