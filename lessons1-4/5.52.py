harvest = 20  # урожайность ячменя в первый год
area = 100  # площадь участка в гектарах в первый год
for year in range(2, 9):
    harvest *= 1.02  # увеличиваем урожайность каждый год на 2%
    if year in [4, 5, 6, 7]:
        area *= 1.05  # увеличиваем площадь участка на 5% в четвертом, пятом, шестом и седьмом годах
    if year <= 6:
        total_harvest = harvest * area  # считаем суммарный урожай за первые шесть лет
    if year <= 8:
        print(f'Урожайность за {year} год: {harvest:.2f}')
    if year in [4, 5, 6, 7]:
        print(f'Площадь участка в {year} год: {area:.2f}')
print(f'Урожай за первые шесть лет: {total_harvest:.2f}')