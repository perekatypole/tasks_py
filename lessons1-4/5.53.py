inner_diameter = 0.1  # внутренний диаметр внутреннего шара в метрах
thickness = 0.005  # толщина стенок шаров в метрах
radius = inner_diameter / 2 + thickness  # радиус внешнего шара
volume = 4 / 3 * 3.14 * radius ** 3  # объем внешнего шара
for i in range(11):
    radius -= thickness  # уменьшаем радиус для следующего шара
    volume += 4 / 3 * 3.14 * radius ** 3  # добавляем объем следующего шара
print(f'Суммарный объем в литрах: {volume*1000:.2f}')