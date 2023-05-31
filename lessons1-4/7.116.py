car_prices = [...]  # список цен на автомобили
motorcycle_prices = [...]  # список цен на мотоциклы
car_avg = sum(car_prices) / len(car_prices)  # среднее арифметическое цен на автомобили
motorcycle_avg = sum(motorcycle_prices) / len(motorcycle_prices)  # среднее арифметическое цен на мотоциклы
if car_avg > 3 * motorcycle_avg:
    print("Средняя стоимость автомобилей превышает среднюю стоимость мотоциклов более чем в 3 раза")
else:
    print("Средняя стоимость автомобилей не превышает среднюю стоимость мотоциклов более чем в 3 раза")