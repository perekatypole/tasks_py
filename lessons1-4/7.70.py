precipitation = [0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0, 0, 0]  # список с количеством осадков
no_precipitation = precipitation.index(max(precipitation)+1, 1)  # количество дней с непрерывными безосадками
print("Количество дней с непрерывными безосадками:", no_precipitation)