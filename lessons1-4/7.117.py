heights = [...]  # список ростов учеников класса (мальчиков и девочек)
boys_heights = [h for h in heights if h < 0]  # список ростов мальчиков
girls_heights = [h for h in heights if h >= 0]  # список ростов девочек
boys_avg = abs(sum(boys_heights) / len(boys_heights))  # модуль среднего арифметического роста мальчиков
girls_avg = sum(girls_heights) / len(girls_heights)  # среднее арифметическое роста девочек
if boys_avg > girls_avg + 10:
    print("Средний рост мальчиков превышает средний рост девочек более чем на 10 см")
else:
    print("Средний рост мальчиков не превышает средний рост девочек более чем на 10 см")