february_rainfalls = [10, 5, 15, 20, 5, 10, 10, 20, 5, 15,
                      5, 10, 10, 15, 20, 5, 10, 10, 15, 20,
                      7, 13, 15, 20, 8, 12, 16, 20, 9, 11]
this_year_rainfall = sum(february_rainfalls)
last_year_rainfall = 250 # примерное количество осадков за февраль прошлого года

if this_year_rainfall > last_year_rainfall:
    print("Количество осадков за этот год превысило прошлогоднее")
else:
    print("В этом году количество осадков не было больше, чем в прошлом")